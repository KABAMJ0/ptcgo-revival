from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import devolve_to_basic

card = ItemCardDef(
    guid="a76df81d-1909-5b5c-b1ca-34866b3651c1",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScoopUp.Name",
    display_name="Scoop Up",
    searchable_by=["Scoop Up"],
    subtypes=[],
    collector_number=78,
    set_code="BASE1",
    rarity=Rarities.Rare,
    effect=devolve_to_basic()
)
