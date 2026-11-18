from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import knocked_out_last_turn, mela_supporter

card = SupporterCardDef(
    guid="9da778cb-a515-55fb-9d75-55bc319dae1f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mela.Name",
    display_name="Mela",
    searchable_by=["Mela", "Supporter"],
    subtypes=["Supporter"],
    collector_number=167,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    effect=mela_supporter(), condition=knocked_out_last_turn()
)
