from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_own_deck

card = ItemCardDef(
    guid="c68e7922-eacb-5303-be3d-5b329584d262",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AlphLithograph.Name",
    display_name="Alph Lithograph",
    searchable_by=["Alph Lithograph", "Item"],
    subtypes=["Item"],
    collector_number=0,
    set_code="HGSS2",
    rarity=Rarities.RareSecret,
    effect=shuffle_own_deck()
)
