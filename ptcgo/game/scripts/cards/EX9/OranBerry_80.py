from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import berry_between_turns

card = PokemonToolCardDef(
    guid="f3bf3d94-6d55-57cd-9dba-f8de08cf1110",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OranBerry.Name",
    display_name="Oran Berry",
    searchable_by=["Oran Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=80,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    granted_abilities=berry_between_turns("Oran Berry", 20, 2)
)
