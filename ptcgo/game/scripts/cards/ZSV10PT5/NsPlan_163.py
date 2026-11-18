from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import move_energy_to_active

card = SupporterCardDef(
    guid="8ed7f020-af1e-58e1-9716-ea90090b20a0",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NsPlan.Name",
    display_name="N's Plan",
    searchable_by=["N's Plan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=163,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    effect=move_energy_to_active(2)
)
