from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_then_draw_energy_bonus

card = SupporterCardDef(
    guid="a21675b6-9b09-5d9d-b191-183260ce7063",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RollerSkater.Name",
    display_name="Roller Skater",
    searchable_by=["Roller Skater", "Supporter"],
    subtypes=["Supporter"],
    collector_number=203,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=discard_then_draw_energy_bonus(2, 2)
)
