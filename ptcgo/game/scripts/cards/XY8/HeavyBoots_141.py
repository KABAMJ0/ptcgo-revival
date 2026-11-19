from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heavy_boots_tool

card = PokemonToolCardDef(
    guid="45cfde93-0bea-5428-b2b2-cc8af213e333",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeavyBoots.Name",
    display_name="Heavy Boots",
    searchable_by=["Heavy Boots", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=141,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=heavy_boots_tool(20, 3),
)
