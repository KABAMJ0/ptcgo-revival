from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_if_stadium

card = SupporterCardDef(
    guid="7fac0e1a-7bd6-558b-990a-cb6425f0a791",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Falkner.Name",
    display_name="Falkner",
    searchable_by=["Falkner", "Supporter"],
    subtypes=["Supporter"],
    collector_number=180,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    effect=draw_if_stadium(2, 2)
)
