from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import strength_charm_tool

card = PokemonToolCardDef(
    guid="60bb2ef7-569c-5a4e-9a75-4c15b17ddcd4",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrengthCharm.Name",
    display_name="Strength Charm",
    searchable_by=["Strength Charm", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=81,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    passive=strength_charm_tool(10, False, True, False),
)
