from ptcgo.game.card_effects.trainers import bench_has_room, furisode_girl
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="70530d2e-89f4-5186-974b-ce59c8d60cb8",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FurisodeGirl.Name",
    display_name="Furisode Girl",
    searchable_by=["Furisode Girl", "Supporter"],
    subtypes=["Supporter"],
    collector_number=190,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    effect=furisode_girl,
    condition=bench_has_room
)
