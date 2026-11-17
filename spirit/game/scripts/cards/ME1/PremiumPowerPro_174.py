from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import turn_damage_boost

card = ItemCardDef(
    guid="39632215-fba0-56b8-baf0-26c30aae5779",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PremiumPowerPro.Name",
    display_name="Premium Power Pro",
    searchable_by=["Premium Power Pro", "Item"],
    subtypes=["Item"],
    collector_number=174,
    set_code="ME1",
    rarity=Rarities.Rare,
    effect=turn_damage_boost(30, pokemon_type="fighting")
)
