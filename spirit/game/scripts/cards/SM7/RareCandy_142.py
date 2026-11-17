from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import evolve_from_hand

card = ItemCardDef(
    guid="3fbf851f-bd03-53b2-a0e0-4210561ea4b9",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=142,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=evolve_from_hand()
)
