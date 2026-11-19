"""The Charizard ex Collection bundle, granted end to end, and decks whose cosmetics
the account does not own."""
import asyncio
import os
import tempfile
import unittest
import uuid
from types import SimpleNamespace

_TMP = tempfile.mkdtemp(prefix="ptcgo_bundle_")
os.environ["PTCGO_ACTIVITY_LOG_DIR"] = _TMP

from ptcgo.database import connection  # noqa: E402

connection.DB_PATH = os.path.join(_TMP, "bundle.db")
connection.engine.dispose()

from ptcgo.database import Base, engine, db_session, Account, Wallet, Collection, Deck  # noqa: E402
from ptcgo.database.accounts import hash_password  # noqa: E402

Base.metadata.create_all(engine)

from ptcgo.game.attributes import AttrID, DefaultCosmetic, ProductType  # noqa: E402
from ptcgo.game.models import product as product_model  # noqa: E402
from ptcgo.game.scripts.cards import loader as card_loader  # noqa: E402
from ptcgo.game.scripts.products import loader as product_loader  # noqa: E402

BUNDLE = str(uuid.uuid5(uuid.NAMESPACE_URL, "ptcgo:product:bundle:charizard-ex-collection"))
CHARIZARD = "087b2bf5-039a-55e8-80c8-899dbb0676a3"
FUSION_STRIKE = "d017c195-83c5-c74e-0638-25128b3116c4"
GOLD_CHARIZARD_COIN = "adb210c2-bca5-5b1a-8b24-c8bcdac41fb8"
PRICE = 500


def new_account(tokens):
    account_id = str(uuid.uuid4())
    with db_session() as s:
        s.add(Account(account_id=account_id, username="u" + account_id[:8], screen_name="U",
                      password_hash=hash_password("x")))
        s.add(Wallet(account_id=account_id, coins=tokens, gems=0, tickets=0))
    return account_id


def collection(account_id):
    with db_session() as s:
        return {r.archetype_id.lower(): r.tradable_count + r.nontradable_count
                for r in s.query(Collection).filter_by(account_id=account_id)}


def tokens(account_id):
    with db_session() as s:
        return s.query(Wallet).filter_by(account_id=account_id).one().coins


def client_for(account_id):
    from ptcgo.game.models.player import Player
    from ptcgo.database.accounts import get_account_by_id
    sent = []

    async def send_packet(packet, request_id=0, flags=0):
        sent.append(packet)
    client = SimpleNamespace(player=Player(get_account_by_id(account_id)), send_packet=send_packet,
                             addr=("127.0.0.1", 1))
    return client, sent


class BundleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        card_loader.load_all()
        product_loader.load_all()
        from ptcgo.database.shop_defaults import ensure_default_shop_items
        from ptcgo.shop import shop_manager
        ensure_default_shop_items()
        shop_manager.reload_from_db(reload_products=False)
        cls.shop = shop_manager.get_shop()
        cls.listing = next(p for p in cls.shop.available_products.values()
                           if cls.shop.resolve_product_guid(p.guid) == BUNDLE)

    def test_the_bundle_is_a_listed_pack_with_three_grants(self):
        bundle = product_loader.products_by_guid[BUNDLE]
        self.assertIsInstance(bundle, product_model.Bundle)
        self.assertNotIsInstance(bundle, product_model.BoosterPack)
        self.assertEqual(bundle.product_type, ProductType.PACKS.value)
        self.assertEqual(bundle.grants, [CHARIZARD, FUSION_STRIKE, GOLD_CHARIZARD_COIN])
        self.assertEqual(bundle.tokens, 1000)
        self.assertTrue(bundle.once_per_account)
        coin = product_loader.products_by_guid[GOLD_CHARIZARD_COIN]
        self.assertEqual((coin.name, coin.product_type), ("ASRBL Gold Charizard Coin", ProductType.COINS.value))
        self.assertEqual(bundle.get_attribute_value(AttrID.IMAGE_NAME), "charizard_ex_collection")
        art = os.path.join(os.path.dirname(product_loader.scripts_dir), "..", "..", "assets", "products",
                           "custom_packs", "charizard_ex_collection.png")
        from PIL import Image
        self.assertEqual(Image.open(art).size, (512, 512))
        card = card_loader.cards_by_guid[CHARIZARD]
        self.assertEqual((card.display_name, card.key, card.get_attribute_value(AttrID.COLLECTOR_NUMBER)),
                         ("Charizard ex", "SV3", 125))
        self.assertEqual(product_loader.products_by_guid[FUSION_STRIKE].name, "Sword & Shield - Fusion Strike")
        self.assertEqual(self.listing.product_type, ProductType.PACKS.value)
        self.assertEqual(self.listing.prices, [{"name": AttrID.TRAINER_TOKENS.value, "value": PRICE}])

    def test_buying_grants_the_card_the_pack_and_the_tokens(self):
        from ptcgo.packets.handlers.shop import ShopHandler
        account_id = new_account(2000)
        client, sent = client_for(account_id)
        asyncio.run(ShopHandler(client).handle_purchase_catalog_products(
            {"selections": [self.listing.guid]}, 3, 0))
        purchased = next(p for p in sent if p.get("messageName") == "ProductsPurchased")
        self.assertEqual(sorted(i["archetypeID"] for i in purchased["items"]),
                         sorted([CHARIZARD, FUSION_STRIKE, GOLD_CHARIZARD_COIN]))
        self.assertEqual(collection(account_id), {CHARIZARD: 1, FUSION_STRIKE: 1, GOLD_CHARIZARD_COIN: 1})
        self.assertEqual(tokens(account_id), 2000 - PRICE + 1000)
        self.assertTrue(any(p.get("messageName") == "CurrentWallet" for p in sent))
        self.assertEqual(client.player.wallet.balances[AttrID.TRAINER_TOKENS], 2500)

        # The granted Fusion Strike pack is an ordinary pack: it opens into SWSH8 cards.
        sent.clear()
        asyncio.run(ShopHandler(client).handle_open_products_by_archetype_id({"products": [FUSION_STRIKE]}, 4, 0))
        opened = next(p for p in sent if p.get("messageName") == "ProductsOpened")
        swsh8 = {c.guid for c in card_loader.cards if c.key == "SWSH8"}
        self.assertTrue(opened["items"] and {i["archetypeID"] for i in opened["items"]} <= swsh8)

    def test_not_enough_tokens_changes_nothing(self):
        from ptcgo.packets.handlers.shop import ShopHandler
        account_id = new_account(PRICE - 1)
        client, sent = client_for(account_id)
        asyncio.run(ShopHandler(client).handle_purchase_catalog_products(
            {"selections": [self.listing.guid]}, 3, 0))
        self.assertTrue(any(p.get("messageName") == "ProductPurchaseFailure" for p in sent))
        self.assertEqual((collection(account_id), tokens(account_id)), ({}, PRICE - 1))

    def test_opening_an_owned_bundle_grants_the_same(self):
        from ptcgo.packets.handlers.shop import ShopHandler
        account_id = new_account(0)
        with db_session() as s:
            s.add(Collection(account_id=account_id, archetype_id=BUNDLE, tradable_count=1, nontradable_count=0))
        client, sent = client_for(account_id)
        asyncio.run(ShopHandler(client).handle_open_products_by_archetype_id({"products": [BUNDLE]}, 5, 0))
        self.assertEqual(collection(account_id), {BUNDLE: 0, CHARIZARD: 1, FUSION_STRIKE: 1, GOLD_CHARIZARD_COIN: 1})
        self.assertEqual(tokens(account_id), 1000)
        self.assertEqual(client.player.wallet.balances[AttrID.TRAINER_TOKENS], 1000)

    def test_one_per_account_second_purchase_is_refused(self):
        from ptcgo.packets.handlers.shop import ShopHandler
        from ptcgo.database.economy_data import PURCHASE_ERROR_ONCE
        account_id = new_account(5000)
        client, sent = client_for(account_id)
        for attempt in (1, 2):
            asyncio.run(ShopHandler(client).handle_purchase_catalog_products(
                {"selections": [self.listing.guid]}, attempt, 0))
        outcomes = [p["messageName"] for p in sent if p.get("messageName") in ("ProductsPurchased", "ProductPurchaseFailure")]
        self.assertEqual(outcomes, ["ProductsPurchased", "ProductPurchaseFailure"])
        failure = next(p for p in sent if p.get("messageName") == "ProductPurchaseFailure")
        self.assertEqual(failure["error"]["id"], PURCHASE_ERROR_ONCE)
        self.assertEqual(collection(account_id), {CHARIZARD: 1, FUSION_STRIKE: 1, GOLD_CHARIZARD_COIN: 1})
        self.assertEqual(tokens(account_id), 5000 - PRICE + 1000)
        # Two in one request is refused outright, and so are the other purchase paths.
        other = new_account(5000)
        client, sent = client_for(other)
        asyncio.run(ShopHandler(client).handle_purchase_catalog_products(
            {"selections": [self.listing.guid, self.listing.guid]}, 1, 0))
        self.assertEqual((collection(other), tokens(other)), ({}, 5000))
        asyncio.run(ShopHandler(client).handle_purchase_archetypes({"archetypes": {self.listing.guid: 1}}, 2, 0))
        asyncio.run(ShopHandler(client).handle_purchase_and_open_products({"products": [self.listing.guid]}, 3, 0))
        asyncio.run(ShopHandler(client).handle_purchase_archetypes({"archetypes": {self.listing.guid: 1}}, 4, 0))
        self.assertEqual(collection(other), {CHARIZARD: 1, FUSION_STRIKE: 1, GOLD_CHARIZARD_COIN: 1})
        self.assertEqual(tokens(other), 5000 - PRICE + 1000)
        failures = [p for p in sent if p.get("messageName") in ("ProductsOpenedFailure", "ArchetypesPurchaseFailure")]
        self.assertEqual(len(failures), 2)

    def test_racing_purchases_only_one_succeeds(self):
        import threading
        from collections import Counter as C
        from ptcgo.database.economy_data import purchase_products
        account_id = new_account(5000)
        start = threading.Barrier(6)
        results = []

        def buy():
            start.wait()
            results.append(purchase_products(
                account_id, {AttrID.TRAINER_TOKENS.value: PRICE},
                C([CHARIZARD, FUSION_STRIKE, GOLD_CHARIZARD_COIN]),
                credit={AttrID.TRAINER_TOKENS.value: 1000}, claims=[BUNDLE]))
        threads = [threading.Thread(target=buy) for _ in range(6)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(results.count(None), 1, results)
        self.assertEqual(collection(account_id), {CHARIZARD: 1, FUSION_STRIKE: 1, GOLD_CHARIZARD_COIN: 1})
        self.assertEqual(tokens(account_id), 5000 - PRICE + 1000)

    def test_a_row_still_at_the_old_price_is_repriced_but_an_admin_price_is_kept(self):
        from ptcgo.database.economy_data import list_shop_items, upsert_shop_item
        from ptcgo.database.shop_defaults import ensure_default_shop_items
        row = lambda: next(r for r in list_shop_items() if r["product_guid"].lower() == BUNDLE)
        upsert_shop_item(BUNDLE, price=1500, item_id=row()["id"])
        ensure_default_shop_items()
        self.assertEqual(row()["price"], PRICE)
        upsert_shop_item(BUNDLE, price=750, item_id=row()["id"])
        ensure_default_shop_items()
        self.assertEqual(row()["price"], 750)
        upsert_shop_item(BUNDLE, price=PRICE, item_id=row()["id"])

    def test_the_bundle_never_auto_lists_at_pack_price(self):
        from ptcgo.shop import shop_manager
        from ptcgo.database.economy_data import list_shop_items, delete_shop_item
        row = next(r for r in list_shop_items() if r["product_guid"].lower() == BUNDLE)
        delete_shop_item(row["id"])
        try:
            shop_manager.reload_from_db(reload_products=False)
            shop = shop_manager.get_shop()
            self.assertFalse(any(shop.resolve_product_guid(g) == BUNDLE for g in shop.available_products))
        finally:
            from ptcgo.database.shop_defaults import ensure_default_shop_items
            ensure_default_shop_items()
            shop_manager.reload_from_db(reload_products=False)


class DeckCosmeticsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        card_loader.load_all()
        product_loader.load_all()
        coins = [p.guid for p in product_loader.products if p.product_type == ProductType.COINS.value
                 and p.guid != DefaultCosmetic.COIN.value]
        cls.owned_coin, cls.lost_coin = coins[0], coins[1]

    def deck(self, coin, sleeve=None):
        attrs = [{"name": AttrID.SELECTED_COIN.value, "value": coin},
                 {"name": AttrID.SELECTED_SLEEVE.value, "value": sleeve or DefaultCosmetic.SLEEVE.value},
                 {"name": AttrID.SELECTED_DECK_BOX.value, "value": DefaultCosmetic.DECK_BOX.value}]
        return {"deckID": str(uuid.uuid4()), "deckName": "Test", "piles": {"deck": [CHARIZARD] * 4},
                "attributes": attrs}

    @staticmethod
    def attr(deck, name):
        return next(a["value"] for a in deck["attributes"] if int(a["name"]) == name.value)

    def test_saving_a_deck_with_an_unowned_coin_saves_the_default(self):
        from ptcgo.packets.handlers.data_sync import DataSyncHandler
        account_id = new_account(0)
        with db_session() as s:
            s.add(Collection(account_id=account_id, archetype_id=self.owned_coin, tradable_count=1, nontradable_count=0))
        client, sent = client_for(account_id)
        handler = DataSyncHandler(client)
        lost = self.deck(self.lost_coin, sleeve=str(uuid.uuid4()))
        asyncio.run(handler.handle_cake_save_deck({"deck": lost}, 1, 0))
        saved = next(p for p in sent if p.get("messageName") == "DeckSaved")["deck"]
        self.assertEqual(self.attr(saved, AttrID.SELECTED_COIN), DefaultCosmetic.COIN.value)
        self.assertEqual(self.attr(saved, AttrID.SELECTED_SLEEVE), DefaultCosmetic.SLEEVE.value)
        with db_session() as s:
            stored = s.query(Deck).filter_by(id=lost["deckID"]).one().deck_data
        self.assertEqual(self.attr(stored, AttrID.SELECTED_COIN), DefaultCosmetic.COIN.value)

        kept = self.deck(self.owned_coin.upper())
        asyncio.run(handler.handle_cake_save_deck({"deck": kept}, 2, 0))
        saved = [p for p in sent if p.get("messageName") == "DeckSaved"][-1]["deck"]
        self.assertEqual(self.attr(saved, AttrID.SELECTED_COIN), self.owned_coin.upper())

    def test_loading_a_stored_deck_with_a_coin_no_longer_owned_sends_the_default(self):
        from ptcgo.game.models.player import Player
        from ptcgo.database.accounts import get_account_by_id
        account_id = new_account(0)
        with db_session() as s:
            s.add(Collection(account_id=account_id, archetype_id=self.owned_coin, tradable_count=1, nontradable_count=0))
            s.add(Deck(id=str(uuid.uuid4()), account_id=account_id, name="Old", deck_data=self.deck(self.lost_coin)))
            s.add(Deck(id=str(uuid.uuid4()), account_id=account_id, name="Fine", deck_data=self.deck(self.owned_coin)))
        player = Player(get_account_by_id(account_id))
        decks = player.get_decks_data()["decks"]
        self.assertEqual(len(decks), 2)
        coins = sorted(self.attr(d, AttrID.SELECTED_COIN) for d in decks)
        self.assertEqual(coins, sorted([DefaultCosmetic.COIN.value, self.owned_coin]))

    def test_a_shipped_deck_keeps_its_deck_box(self):
        from ptcgo.game.decks.cosmetics import allowed_cosmetics, fix_deck_cosmetics
        boxes = {str(p.deck_box).lower() for p in product_loader.products if getattr(p, "deck_box", None)}
        self.assertTrue(boxes)
        deck = self.deck(DefaultCosmetic.COIN.value)
        deck["attributes"][2]["value"] = next(iter(boxes))
        self.assertEqual(fix_deck_cosmetics(deck, allowed_cosmetics(new_account(0))), [])


if __name__ == "__main__":
    unittest.main()
