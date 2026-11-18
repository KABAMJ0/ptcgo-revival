from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_may_draw_up_to

card = ItemCardDef(
    guid="c3978618-8737-5605-94d5-e09c82e3f262",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Erika.Name",
    display_name="Erika",
    searchable_by=["Erika"],
    subtypes=[],
    collector_number=16,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    effect=each_may_draw_up_to(3)
)
