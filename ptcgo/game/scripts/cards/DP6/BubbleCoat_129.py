from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import bubble_coat_tool

card = PokemonToolCardDef(
    guid="44f3496a-7286-530d-b131-a494f9bc8393",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BubbleCoat.Name",
    display_name="Bubble Coat",
    searchable_by=["Bubble Coat", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=129,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    passive=bubble_coat_tool(),
)
