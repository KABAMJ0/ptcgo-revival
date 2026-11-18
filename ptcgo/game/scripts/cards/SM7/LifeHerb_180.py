from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_heal_cure

card = ItemCardDef(
    guid="bf702ca9-b6b6-5726-b53d-00fb3670569f",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeHerb.Name",
    display_name="Life Herb",
    searchable_by=["Life Herb", "Item"],
    subtypes=["Item"],
    collector_number=180,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    effect=flip_heal_cure(None, 60)
)
