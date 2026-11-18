from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import strength_charm_tool

card = PokemonToolCardDef(
    guid="656950fa-b639-5bb2-9557-215aed817e77",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrengthCharm.Name",
    display_name="Strength Charm",
    searchable_by=["Strength Charm", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=74,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    passive=strength_charm_tool(10, True, True, True),
)
