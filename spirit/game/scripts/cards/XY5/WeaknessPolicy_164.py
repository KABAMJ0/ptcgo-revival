from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import holder_no_weakness

card = PokemonToolCardDef(
    guid="59aa7819-4930-56c9-b6c5-200dc6d4f3eb",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WeaknessPolicy.Name",
    display_name="Weakness Policy",
    searchable_by=["Weakness Policy", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=164,
    set_code="XY5",
    rarity=Rarities.RareSecret,
    passive=holder_no_weakness()
)
