from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_cure_and_heal_active

card = ItemCardDef(
    guid="644d3e22-e44d-58b6-b4ea-715016f5fe23",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HealPowder.Name",
    display_name="Heal Powder",
    searchable_by=["Heal Powder"],
    subtypes=[],
    collector_number=104,
    set_code="NEO4",
    rarity=Rarities.Common,
    effect=flip_cure_and_heal_active(2)
)
