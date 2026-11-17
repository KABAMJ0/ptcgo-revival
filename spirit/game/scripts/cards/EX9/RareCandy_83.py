from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import evolve_from_hand

card = ItemCardDef(
    guid="a0f811ac-c221-5621-b316-16c9b716e6b1",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=83,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    effect=evolve_from_hand()
)
