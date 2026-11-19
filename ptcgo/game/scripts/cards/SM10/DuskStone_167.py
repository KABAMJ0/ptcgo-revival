from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_from_deck, named_one_of


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
    effect=evolve_from_deck(named_one_of(
        "Mismagius", "Honchkrow", "Chandelure", "Aegislash")),
)
