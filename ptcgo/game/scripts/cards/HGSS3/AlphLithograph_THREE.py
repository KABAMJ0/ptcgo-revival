from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import return_stadium_to_hand

card = ItemCardDef(
    guid="12867848-b64c-5cdd-aa7d-6ab5ce1a7fa4",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AlphLithograph.Name",
    display_name="Alph Lithograph",
    searchable_by=["Alph Lithograph", "Item"],
    subtypes=["Item"],
    collector_number=0,
    set_code="HGSS3",
    rarity=Rarities.RareSecret,
    effect=return_stadium_to_hand()
)
