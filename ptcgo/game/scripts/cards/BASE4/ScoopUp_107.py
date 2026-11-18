from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import devolve_to_basic

card = ItemCardDef(
    guid="f7a97997-9557-5ac0-8e72-cfa42680a4ab",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScoopUp.Name",
    display_name="Scoop Up",
    searchable_by=["Scoop Up"],
    subtypes=[],
    collector_number=107,
    set_code="BASE4",
    rarity=Rarities.Rare,
    effect=devolve_to_basic()
)
