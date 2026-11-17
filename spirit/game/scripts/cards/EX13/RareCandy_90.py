from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import evolve_from_hand

card = ItemCardDef(
    guid="0b5ad6a3-5c69-53fc-ae6b-196e8e09b6d7",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    effect=evolve_from_hand()
)
