from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import look_at_own_prizes

card = ItemCardDef(
    guid="69295f38-dcd3-5cc6-8633-0d9a8f716d64",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AlphLithograph.Name",
    display_name="Alph Lithograph",
    searchable_by=["Alph Lithograph", "Item"],
    subtypes=["Item"],
    collector_number=0,
    set_code="HGSS4",
    rarity=Rarities.RareSecret,
    effect=look_at_own_prizes()
)
