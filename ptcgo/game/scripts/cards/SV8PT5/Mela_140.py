from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import knocked_out_last_turn, mela_supporter

card = SupporterCardDef(
    guid="993fc9c3-240b-58fc-b35d-ea75bb104bb3",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mela.Name",
    display_name="Mela",
    searchable_by=["Mela", "Supporter"],
    subtypes=["Supporter"],
    collector_number=140,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=mela_supporter(), condition=knocked_out_last_turn()
)
