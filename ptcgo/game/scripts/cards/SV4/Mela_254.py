from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import knocked_out_last_turn, mela_supporter

card = SupporterCardDef(
    guid="d4f9cb5e-70df-5c98-911d-af42a6eb0b47",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mela.Name",
    display_name="Mela",
    searchable_by=["Mela", "Supporter"],
    subtypes=["Supporter"],
    collector_number=254,
    set_code="SV4",
    rarity=Rarities.Rare,
    effect=mela_supporter(), condition=knocked_out_last_turn()
)
