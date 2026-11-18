from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import devolve_highest_to_hand

card = ItemCardDef(
    guid="45a8e691-0dd2-5026-8712-8cea3524b029",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HyperDevolutionSpray.Name",
    display_name="Hyper Devolution Spray",
    searchable_by=["Hyper Devolution Spray"],
    subtypes=[],
    collector_number=73,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    effect=devolve_highest_to_hand()
)
