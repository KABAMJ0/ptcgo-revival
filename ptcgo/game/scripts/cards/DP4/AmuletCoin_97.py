from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import end_of_turn_while_active_tool

card = PokemonToolCardDef(
    guid="b0151dd5-68b4-5509-8def-0c9415905bae",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AmuletCoin.Name",
    display_name="Amulet Coin",
    searchable_by=["Amulet Coin", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=97,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    granted_abilities=end_of_turn_while_active_tool('Amulet Coin', 1, 0),
)
