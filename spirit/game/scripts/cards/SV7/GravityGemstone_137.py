from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import active_holder_retreat_tax

card = PokemonToolCardDef(
    guid="13f5798c-8e71-51a3-afdd-a64951e9fdbb",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GravityGemstone.Name",
    display_name="Gravity Gemstone",
    searchable_by=["Gravity Gemstone", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=137,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    passive=active_holder_retreat_tax(1)
)
