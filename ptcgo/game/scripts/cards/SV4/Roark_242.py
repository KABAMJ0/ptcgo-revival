from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_recover_basic_energy

card = SupporterCardDef(
    guid="087fee62-7be9-5658-a64d-dcb6745c1e90",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Roark.Name",
    display_name="Roark",
    searchable_by=["Roark", "Supporter"],
    subtypes=["Supporter"],
    collector_number=242,
    set_code="SV4",
    rarity=Rarities.Rare,
    effect=draw_then_recover_basic_energy(2, 1)
)
