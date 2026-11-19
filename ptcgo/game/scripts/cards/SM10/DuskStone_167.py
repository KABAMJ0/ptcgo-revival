from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_any, evolve_from_deck_matching

_DUSK_STONE_EVOLUTIONS = card_named_any(
    ("mismagius", "honchkrow", "chandelure", "aegislash"))


card = ItemCardDef(
    guid="583fe190-63d2-51b2-b0cd-cab473610326",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DuskStone.Name",
    display_name="Dusk Stone",
    searchable_by=["Dusk Stone", "Item"],
    subtypes=["Item"],
    collector_number=167,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=evolve_from_deck_matching(_DUSK_STONE_EVOLUTIONS)
)
