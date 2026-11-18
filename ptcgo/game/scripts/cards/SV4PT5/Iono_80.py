from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_draw_per_prize

card = SupporterCardDef(
    guid="dcd43107-fddb-5d4d-8076-ef4a93370397",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Iono.Name",
    display_name="Iono",
    searchable_by=["Iono", "Supporter"],
    subtypes=["Supporter"],
    collector_number=80,
    set_code="SV4PT5",
    rarity=Rarities.Uncommon,
    effect=each_player_shuffle_draw_per_prize()
)
