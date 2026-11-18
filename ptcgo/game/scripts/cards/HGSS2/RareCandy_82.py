from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_from_hand

card = ItemCardDef(
    guid="55ed0c69-c2c5-5b24-9e65-d71f15f22c14",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="HGSS2",
    rarity=Rarities.Uncommon,
    effect=evolve_from_hand()
)
