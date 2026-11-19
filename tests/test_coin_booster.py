"""Coin Booster: a pack of 10 different coins, granted end to end through the shop."""
import asyncio
import os
import tempfile
import unittest
import uuid
from collections import Counter
from types import SimpleNamespace

_TMP = tempfile.mkdtemp(prefix="ptcgo_coin_booster_")
os.environ["PTCGO_ACTIVITY_LOG_DIR"] = _TMP

from ptcgo.database import connection  # noqa: E402

connection.DB_PATH = os.path.join(_TMP, "coin_booster.db")
connection.engine.dispose()

from ptcgo.database import Base, engine, db_session, Account, Wallet, Collection  # noqa: E402
from ptcgo.database.accounts import hash_password  # noqa: E402

Base.metadata.create_all(engine)

from ptcgo.game.attributes import AttrID, DefaultCosmetic, ProductType  # noqa: E402
from ptcgo.game.models import product as product_model  # noqa: E402
from ptcgo.game.scripts.cards import loader as card_loader  # noqa: E402
from ptcgo.game.scripts.products import loader as product_loader  # noqa: E402

COIN_BOOSTER = str(uuid.uuid5(uuid.NAMESPACE_URL, "ptcgo:product:COINBOOSTER"))


def coin_guids():
    return {p.guid for p in product_loader.products if p.product_type == ProductType.COINS.value}


class CoinBoosterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        card_loader.load_all()
        product_loader.load_all()

    def test_the_product_is_a_pack(self):
        pack = product_loader.products_by_guid[COIN_BOOSTER]
        self.assertIsInstance(pack, product_model.BoosterPack)
        self.assertEqual(pack.product_type, ProductType.PACKS.value)
        self.assertEqual(pack.name, "Coin Booster")
        # Base Set's own set attributes, so the client renders and opens it like a booster.
        base = next(p for p in product_loader.products
                    if p.key == "BASE1" and p.guid != COIN_BOOSTER and p.product_type == ProductType.PACKS.value)
        for attr in (AttrID.SET_KEY, AttrID.SET_CACHE_KEY, AttrID.EXPANSION):
            self.assertEqual(pack.get_attribute_value(attr), "BASE1", attr)
            self.assertEqual(pack.get_attribute_value(attr), base.get_attribute_value(attr), attr)
        self.assertEqual(pack.get_attribute_value(AttrID.IMAGE_NAME), "base1_booster")
        self.assertTrue(os.path.exists(os.path.join(
            os.path.dirname(product_loader.scripts_dir), "..", "..", "assets", "products",
            "custom_packs", "base1_booster.png")))

    def test_a_real_base_set_booster_still_opens_cards(self):
        base = next(p for p in product_loader.products
                    if p.key == "BASE1" and p.guid != COIN_BOOSTER and p.product_type == ProductType.PACKS.value)
        cards = {c.guid for c in card_loader.cards if c.key == "BASE1"}
        contents = base.open("-1")
        self.assertTrue(contents and set(contents) <= cards, contents)

    def test_every_pack_is_ten_different_coins(self):
        pack = product_loader.products_by_guid[COIN_BOOSTER]
        coins = coin_guids()
        self.assertGreater(len(coins), 1000)
        for _ in range(300):
            contents = pack.open("-1")
            self.assertEqual(len(contents), 10)
            self.assertEqual(len(set(contents)), 10, "a pack repeated a coin")
            self.assertTrue(set(contents) <= coins, set(contents) - coins)
            self.assertNotIn(DefaultCosmetic.COIN.value, contents)

    def test_gold_coins_are_rarer_than_their_share(self):
        pack = product_loader.products_by_guid[COIN_BOOSTER]
        coins = [p for p in product_loader.products if p.product_type == ProductType.COINS.value
                 and p.guid != DefaultCosmetic.COIN.value]
        gold = {p.guid for p in coins if product_model.coin_weight(p) < 0.5}
        share = len(gold) / len(coins)
        drawn = Counter(g in gold for _ in range(400) for g in pack.open("-1"))
        self.assertLess(drawn[True] / sum(drawn.values()), share * 0.75)

    def test_buying_and_opening_grants_ten_coins(self):
        from ptcgo.database.shop_defaults import ensure_default_shop_items
        from ptcgo.game.models.player import Player
        from ptcgo.database.accounts import get_account_by_id
        from ptcgo.database.player_data import get_merged_collection_payload
        from ptcgo.packets.handlers.shop import ShopHandler
        from ptcgo.shop import shop_manager

        account_id = str(uuid.uuid4())
        with db_session() as s:
            s.add(Account(account_id=account_id, username="coinfan", screen_name="Coinfan",
                          password_hash=hash_password("x")))
            s.add(Wallet(account_id=account_id, coins=5, gems=0, tickets=0))
        ensure_default_shop_items()
        shop_manager.reload_from_db(reload_products=False)
        shop = shop_manager.get_shop()
        listing = next(p for p in shop.available_products.values()
                       if shop.resolve_product_guid(p.guid) == COIN_BOOSTER)
        self.assertEqual(listing.product_type, ProductType.PACKS.value)  # Booster Packs tab
        self.assertEqual(listing.prices, [{"name": AttrID.TRAINER_TOKENS.value, "value": 1}])

        sent = []

        async def send_packet(packet, request_id=0, flags=0):
            sent.append(packet)
        client = SimpleNamespace(player=Player(get_account_by_id(account_id)), send_packet=send_packet,
                                 addr=("127.0.0.1", 1))
        before = {r["archetypeID"]: r for r in get_merged_collection_payload(account_id)}
        asyncio.run(ShopHandler(client).handle_purchase_and_open_products(
            {"products": [listing.guid]}, 7, 0))

        opened = next(p for p in sent if p.get("messageName") == "ProductsOpened")
        granted = [item["archetypeID"] for item in opened["items"]]
        self.assertEqual(len(granted), 10)
        self.assertTrue(set(granted) <= coin_guids())
        with db_session() as s:
            rows = {r.archetype_id: r.tradable_count + r.nontradable_count
                    for r in s.query(Collection).filter_by(account_id=account_id)}
            self.assertEqual(s.query(Wallet).filter_by(account_id=account_id).one().coins, 4)
        self.assertEqual(sum(rows.get(g, 0) for g in set(granted)), 10)
        self.assertEqual(sum(rows.values()), 10, rows)
        after = {r["archetypeID"]: r for r in get_merged_collection_payload(account_id)}
        for guid in granted:
            self.assertNotIn(guid.lower(), before)
            self.assertEqual(after[guid.lower()]["tradable"], 1)  # owned, so selectable as a deck coin
        self.assertTrue(any(p.get("messageName") == "CollectionCountFound" for p in sent))


if __name__ == "__main__":
    unittest.main()
