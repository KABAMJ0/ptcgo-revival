from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard, search_to_hand
from spirit.game.card_effects.trainers import choose_one, named_exactly

card = ItemCardDef(
    guid="6b7d0bfc-a78a-5fd6-9d2d-bf502534705e",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilExcavationMap.Name",
    display_name="Fossil Excavation Map",
    searchable_by=["Fossil Excavation Map", "Item"],
    subtypes=["Item"],
    collector_number=107,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    effect=choose_one([("Search your deck for an Unidentified Fossil card, reveal it, and put i", search_to_hand(named_exactly("Unidentified Fossil"), count=1)), ("Put an Unidentified Fossil card from your discard pile into your hand", recover_from_discard(named_exactly("Unidentified Fossil"), count=1, to="hand"))])
)
