from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_from_hand

card = ItemCardDef(
    guid="ddf1f204-3901-5a6b-b22d-01e558e84584",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=165,
    set_code="SM2",
    rarity=Rarities.RareSecret,
    effect=evolve_from_hand()
)
