from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_if_stadium

card = SupporterCardDef(
    guid="1d4cd76c-4f76-598e-bc84-473483c06bb3",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Falkner.Name",
    display_name="Falkner",
    searchable_by=["Falkner", "Supporter"],
    subtypes=["Supporter"],
    collector_number=251,
    set_code="SV2",
    rarity=Rarities.Rare,
    effect=draw_if_stadium(2, 2)
)
