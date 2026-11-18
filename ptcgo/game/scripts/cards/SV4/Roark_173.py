from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_recover_basic_energy

card = SupporterCardDef(
    guid="50eab561-24b0-5f10-a280-aeda11b61202",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Roark.Name",
    display_name="Roark",
    searchable_by=["Roark", "Supporter"],
    subtypes=["Supporter"],
    collector_number=173,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    effect=draw_then_recover_basic_energy(2, 1)
)
