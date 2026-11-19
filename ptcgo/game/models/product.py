import json
import copy
import uuid
import random
import logging
from typing import Any, Optional, Dict, List
from ptcgo.game.attributes import AttrID, ProductType, CardType, Rarities, DefaultCosmetic, DeckBoxShape
from ptcgo.game.models.card import Card
import ptcgo.server.state as state
from ptcgo.game.scripts.cards import loader as card_loader
from ptcgo.game.content import pack_rules

SHOP_SKU_NAMESPACE = uuid.uuid5(uuid.NAMESPACE_DNS, "spiritptcgo.shop.sku")


def make_shop_sku(product: "Product") -> "Product":
    """A shop-facing alias of a product with its own GUID, so the client's dynamic-archetype
    eviction on shop exit (ClearDynamicArchetypes) never touches the owned collection GUID."""
    sku_guid = str(uuid.uuid5(SHOP_SKU_NAMESPACE, product.guid))
    attrs = copy.deepcopy(product.attributes)
    attrs[str(AttrID.ARCHETYPE_ID.value)] = {"type": "uuid", "value": sku_guid}
    attrs[str(AttrID.CATALOG_ID.value)] = {"type": "string", "value": sku_guid}
    return Product(sku_guid, product.key, attrs, [dict(p) for p in product.prices])

def safe_int(value: Any, default: int = 0) -> int:
    if value is None:
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

class Product:
    """Models a single product (Pack, Deck, Coin, etc.) in the server."""
    def __init__(self, guid: str, key: str, attributes: Optional[Dict[str, Any]] = None, prices: Optional[List[Dict[str, Any]]] = None):
        self.guid = guid
        self.key = key
        self.attributes = attributes or {}
        self.prices = prices or []

    def get_attribute_value(self, attr_id: AttrID, default: Any = None) -> Any:
        # Handle both AttrID and int/str
        attr_key = str(attr_id.value if isinstance(attr_id, AttrID) else attr_id)
        attr = self.attributes.get(attr_key)
        if attr:
            val = attr.get("value")
            # If it's a JSON type, it might be a string that needs parsing for some uses,
            # but usually for game logic we want the parsed version.
            if attr.get("type") == "json" and isinstance(val, str):
                try:
                    return json.loads(val)
                except:
                    return val
            return val if val is not None else default
        return default

    @property
    def product_type(self) -> int:
        return safe_int(self.get_attribute_value(AttrID.PRODUCT_TYPE, ProductType.UNSET.value))

    @property
    def name(self) -> str:
        name_data = self.get_attribute_value(AttrID.NAME)
        if isinstance(name_data, dict):
            return name_data.get("id", "")
        return str(name_data or "")

    @property
    def catalog_id(self) -> str:
        return str(self.get_attribute_value(AttrID.CATALOG_ID, ""))

    def to_archetype_dict(self) -> Dict[str, Any]:
        """Formats for ArchetypesFound (Protobuf). Keep wrapped for ProtoMessage."""
        return {
            "guid": self.guid,
            "key": self.key,
            "attributes": self.attributes
        }

    def to_archetype_json(self) -> Dict[str, Any]:
        """Serializes the product to the client's Archetype JSON format (Legacy Shop)."""
        attrs = []
        for name_str, attr_data in self.attributes.items():
            val = attr_data.get("value")
            
            # Shop JSON packets expect JSON attributes to be actual JSON objects/dicts, not strings
            if attr_data.get("type") == "json" and isinstance(val, str):
                try:
                    val = json.loads(val)
                except:
                    pass
            attrs.append({"name": int(name_str), "value": val})

        return {
            "archetypeID": self.guid,
            "attributes": attrs
        }

    def get_price_json(self) -> Dict[str, Any]:
        """Serializes the product's price for the AvailableProducts priceMap."""
        return {
            "name": AttrID.SHOP_PRICE_MAP.value,
            "value": self.prices
        }

    def open(self, account_id: str) -> list[str]:
        """Logic for opening the product. Returns list of Archetype GUIDs."""
        return []

class BoosterPack(Product):
    def __init__(self, guid: str, key: str, attributes: Optional[Dict[str, Any]] = None, prices: Optional[List[Dict[str, Any]]] = None):
        super().__init__(guid, key, attributes, prices)
        # Default card pool for BW1 boosters if not specified
        self.card_pool = [
            "7f4966fd-4082-5e69-1855-fee0e79f0ffa",
            "7167880e-4d58-c350-8cc7-adab87e8c6f7",
            "68975361-b02b-330e-b4e3-98c3b8e4bcda",
            "383f19f1-cb84-085b-63cc-e1d14b062cf6",
            "3202abdb-b395-f0c9-9b15-d10187c68255",
            "b7b3e2a1-385f-1466-7dae-47c081ff4626",
            "8597f163-fb9d-980d-32bc-38edc02852ff",
            "338b9be4-7534-1268-5aa4-2663a605d657",
            "eb6ebb86-4606-d7cb-22c4-196d294d0794",
            "96e32e96-f9b0-5157-21ba-9cd01fd43ff3"
        ]

    def open(self, account_id: str) -> list[str]:
        # Get all cards in the game
        all_cards = card_loader.cards
        
        # 1. Filter cards belonging to this set key (e.g., "SWSH8")
        set_cards = [c for c in all_cards if c.key.lower() == self.key.lower()]
        
        if not set_cards:
            # Fallback to default card pool if the set has no cards loaded
            if not self.card_pool:
                return []
            return random.choices(self.card_pool, k=10)
            
        # Helper to safely extract integer values
        def get_attr_int(c, attr):
            val = c.get_attribute_value(attr)
            if val is None:
                return -1
            try:
                return int(val)
            except:
                return -1
            
        def pick_random(card_pool: list[Card], count: int, set_key: str = "") -> list[str]:
            """Pick random cards from a pool considering rarity, scaled by any per-set weight rule"""
            card_guids = []
            weights = []

            for c in card_pool:
                rarity = get_attr_int(c, AttrID.RARITY)
                weight = 1.0

                if rarity >= Rarities.RareHoloEX.value and rarity <= Rarities.RareHoloVSTAR.value:
                    weight = 0.45
                elif rarity == Rarities.RareUltra.value:
                    weight = 0.2
                elif rarity == Rarities.RareSecret.value or rarity == Rarities.RareRainbow.value:
                    weight = 0.1

                if set_key:
                    weight *= pack_rules.multiplier_for(set_key, c)

                weights.append(weight)
                card_guids.append(c.guid)

            return random.choices(card_guids, k=count, weights=weights)

        def assemble_pack_contents(set_key: str):
            commons = [
                c for c in set_cards 
                if get_attr_int(c, AttrID.CARD_TYPE) != CardType.ENERGY.value 
                and get_attr_int(c, AttrID.RARITY) == Rarities.Common.value
            ]
            
            uncommons = [
                c for c in set_cards 
                if get_attr_int(c, AttrID.CARD_TYPE) != CardType.ENERGY.value 
                and get_attr_int(c, AttrID.RARITY) == Rarities.Uncommon.value
            ]

            rares = [
                c for c in set_cards 
                if get_attr_int(c, AttrID.CARD_TYPE) != CardType.ENERGY.value 
                and (get_attr_int(c, AttrID.RARITY) == Rarities.Rare.value 
                    or get_attr_int(c, AttrID.RARITY) == Rarities.RareHolo.value)
            ]

            hits = [
                c for c in set_cards 
                if get_attr_int(c, AttrID.CARD_TYPE) != CardType.ENERGY.value 
                and get_attr_int(c, AttrID.RARITY) >= Rarities.Rare.value
            ]

            # Basic energies in this set
            basic_energies = [
                c for c in set_cards 
                if get_attr_int(c, AttrID.CARD_TYPE) == CardType.ENERGY.value 
                and not c.get_attribute_value(AttrID.IS_SPECIAL_ENERGY)
            ]
            
            # If set has no basic energies, find them in Free_Energy
            if not basic_energies:
                basic_energies = [
                    c.guid for c in all_cards 
                    if c.key.lower() == "free_energy" 
                    and get_attr_int(c, AttrID.CARD_TYPE) == CardType.ENERGY.value 
                    and not c.get_attribute_value(AttrID.IS_SPECIAL_ENERGY)
                ]
                
            # Reverse holos can be any card from this set (excluding Energy)
            reverse_holos = [
                c for c in set_cards 
                if get_attr_int(c, AttrID.CARD_TYPE) != CardType.ENERGY.value
                    and get_attr_int(c, AttrID.CARD_TYPE) != CardType.ENERGY.value
                    and get_attr_int(c, AttrID.RARITY) <= Rarities.Rare.value
            ]

            reverse_hit_rares = [
                # Add SIRs and IRs for Scarlet & Violet
                Rarities.RareRadiant.value,
                Rarities.Ace.value,
                Rarities.Amazing.value,
                Rarities.BreakRare.value,
            ]

            reverse_holos_and_hits = [
                c for c in set_cards 
                if get_attr_int(c, AttrID.CARD_TYPE) != CardType.ENERGY.value
                    and get_attr_int(c, AttrID.CARD_TYPE) != CardType.ENERGY.value
                    and (get_attr_int(c, AttrID.RARITY) <= Rarities.Rare.value
                         or get_attr_int(c, AttrID.RARITY) in reverse_hit_rares)
            ]
            
            # Fallback mappings in case a specific pool is empty due to incomplete script loads
            fallback_set_guids = set_cards
            commons_pool = commons if commons else fallback_set_guids
            uncommons_pool = uncommons if uncommons else fallback_set_guids
            rares_pool = rares if rares else fallback_set_guids
            hits_pool = hits if hits else fallback_set_guids
            energy_pool = basic_energies if basic_energies else fallback_set_guids
            # if the pack is from Scarlet & Violet or newer, add a card from rev_holo_slot_1_pool and remove an uncommon card
            rev_holo_slot_1_pool = reverse_holos if reverse_holos else fallback_set_guids
            rev_holo_slot_2_pool = reverse_holos_and_hits if reverse_holos else fallback_set_guids

            # Per-set rules: cards reserved for a guaranteed slot are kept out of the
            # random pools so a pack can never hold one twice.
            set_rules = pack_rules.rules_for(set_key)
            reserved_names = {n.strip() for n in set_rules.get("exclude_from_random") or []}
            if reserved_names:
                def keep(c):
                    return pack_rules.name_of(c) not in reserved_names

                def narrowed(pool):
                    filtered = [c for c in pool if keep(c)]
                    return filtered if len(filtered) >= 4 else pool

                commons_pool = narrowed(commons_pool)
                uncommons_pool = narrowed(uncommons_pool)
                rares_pool = narrowed(rares_pool)
                hits_pool = narrowed(hits_pool)
                rev_holo_slot_1_pool = narrowed(rev_holo_slot_1_pool)
                rev_holo_slot_2_pool = narrowed(rev_holo_slot_2_pool)

            pack_guids = []
        
            # Celebrations really did give 4 cards a pack; the branch stays behind an
            # opt-in rule so fixing the set-key lookup above did not silently change it.
            if set_key == "CEL25" and set_rules.get("four_card_pack"):
                # Celebrations only has 4 cards

                # 2 Rares Holos
                pack_guids.extend(pick_random(rares_pool, 2, set_key))

                # 1 Reverse Holo - a chance it's a card from the celebrations classic collection
                pack_guids.extend(pick_random(rev_holo_slot_2_pool, 1, set_key))

                # 1 Rare Holo / Hit
                pack_guids.extend(pick_random(hits_pool, 1, set_key))
            else:
                # A real product does not always hold ten cards: a Base Set booster
                # held eleven and a McDonald's promo pack five. A set may declare its
                # slots in pack_rules.json; everything else keeps 4/4/1/1.
                slots = set_rules.get("slots") or {}
                commons_n = int(slots.get("common", 4))
                uncommons_n = int(slots.get("uncommon", 4))
                holo_n = int(slots.get("reverse_holo", 1))
                hits_n = int(slots.get("hit", 1))

                pack_guids.extend(pick_random(commons_pool, commons_n, set_key))
                pack_guids.extend(pick_random(uncommons_pool, uncommons_n, set_key))
                if holo_n:
                    pack_guids.extend(pick_random(rev_holo_slot_2_pool, holo_n, set_key))
                if hits_n:
                    pack_guids.extend(pick_random(hits_pool, hits_n, set_key))

            if set_rules:
                pack_guids = apply_set_rules(set_key, pack_guids, set_cards, commons_pool)
            return pack_guids

        def apply_set_rules(set_key: str, pack_guids: list[str], set_cards, refill_pool) -> list[str]:
            """Enforce a set's pack rules on one assembled pack: drop repeats of a name
            that may appear once, keep the pack at its usual size, and place the
            guaranteed cards in the final (rare) slot."""
            cards_by_guid = {c.guid: c for c in set_cards}
            size = len(pack_guids)
            pack_guids = pack_rules.dedupe(pack_guids, cards_by_guid, set_key)

            unique_names = {n.strip() for n in (pack_rules.rules_for(set_key).get("unique_per_pack") or [])}
            while len(pack_guids) < size and refill_pool:
                candidate = pick_random(refill_pool, 1, set_key)[0]
                card = cards_by_guid.get(candidate)
                if card is not None and pack_rules.name_of(card) in unique_names \
                        and candidate in pack_guids:
                    continue
                pack_guids.append(candidate)

            for pool in pack_rules.guaranteed_picks(set_key, set_cards):
                if pack_guids:
                    pack_guids.pop()
                pack_guids.append(random.choice(pool).guid)
            return pack_guids

        set_key_attribute = str(AttrID.SET_KEY)
        set_key_dict: dict = self.attributes.get(set_key_attribute) or {}
        # The set key decides per-set pack composition; it used to read from the wrong
        # dict and came back empty for every product, so no set-specific rule ever ran.
        set_key: str = str(set_key_dict.get("value") or self.key or "")

        # 2. Assemble the pack (10 cards ordered from common up to rare)
        pack_guids = assemble_pack_contents(set_key)
        return pack_guids

class DeckBox(Product):
    def __init__(self, guid: str, key: str, attributes: Optional[Dict[str, Any]] = None,
                 prices: Optional[List[Dict[str, Any]]] = None, *, shape=DeckBoxShape.TWO_TONE):
        super().__init__(guid, key, attributes, prices)
        self.shape = shape

class Deck(Product):
    def __init__(self, guid: str, key: str, attributes: Optional[Dict[str, Any]] = None,
                 prices: Optional[List[Dict[str, Any]]] = None, *, contents=(),
                 is_theme_deck=False, theme_legal=False, deck_box=None):
        super().__init__(guid, key, attributes, prices)
        self.contents = tuple(contents)
        self.deck_box = deck_box
        self.is_theme_deck = is_theme_deck
        self.theme_legal = theme_legal

    def open(self, account_id: str) -> list[str]:
        return list(self.contents)

    def to_deck_dict(self, deck_id=None):
        """Builds the client's saved-deck payload from the product's card list."""
        return {
            "deckID": deck_id or str(uuid.uuid4()), "deckName": self.name,
            "piles": {"deck": list(self.contents)},
            "attributes": [
                {"name": AttrID.IS_THEME_DECK.value,
                 "value": self.is_theme_deck and self.theme_legal},
                {"name": AttrID.SELECTED_COIN.value, "value": DefaultCosmetic.COIN.value},
                {"name": AttrID.SELECTED_SLEEVE.value, "value": DefaultCosmetic.SLEEVE.value},
                {"name": AttrID.SELECTED_DECK_BOX.value,
                 "value": self.deck_box or DefaultCosmetic.DECK_BOX.value},
            ],
        }
