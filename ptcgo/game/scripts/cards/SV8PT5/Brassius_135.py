from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import count_hand_shuffle_draw_plus

card = SupporterCardDef(
    guid="78a2208c-763c-590b-b237-f1f40022bcb1",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brassius.Name",
    display_name="Brassius",
    searchable_by=["Brassius", "Supporter"],
    subtypes=["Supporter"],
    collector_number=135,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=count_hand_shuffle_draw_plus(1)
)
