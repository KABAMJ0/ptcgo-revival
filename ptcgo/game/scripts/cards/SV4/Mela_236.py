from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import knocked_out_last_turn, mela_supporter

card = SupporterCardDef(
    guid="6588ba90-7ec1-51e2-a461-05dffcf00143",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mela.Name",
    display_name="Mela",
    searchable_by=["Mela", "Supporter"],
    subtypes=["Supporter"],
    collector_number=236,
    set_code="SV4",
    rarity=Rarities.Rare,
    effect=mela_supporter(), condition=knocked_out_last_turn()
)
