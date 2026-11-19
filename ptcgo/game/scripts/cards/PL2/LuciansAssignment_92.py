from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import move_energy_freely_between_own

card = SupporterCardDef(
    guid="e32dce40-ea28-5fa2-b962-cc8e13e29a60",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuciansAssignment.Name",
    display_name="Lucian's Assignment",
    searchable_by=["Lucian's Assignment", "Supporter"],
    subtypes=["Supporter"],
    collector_number=92,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    effect=move_energy_freely_between_own()
)
