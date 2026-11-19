from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import berry_between_turns

card = PokemonToolCardDef(
    guid="6a4b0b44-0dd5-571e-9423-3a6f1f4e37d4",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OranBerry.Name",
    display_name="Oran Berry",
    searchable_by=["Oran Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=85,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    granted_abilities=berry_between_turns('Oran Berry', 20, 2),
)
