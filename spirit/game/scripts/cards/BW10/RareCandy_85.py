from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import evolve_from_hand

card = ItemCardDef(
    guid="330b636a-d948-5b62-af0c-1814e0ababca",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=85,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=evolve_from_hand()
)
