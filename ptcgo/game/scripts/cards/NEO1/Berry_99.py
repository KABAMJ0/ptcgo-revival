from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import berry_between_turns

card = PokemonToolCardDef(
    guid="0c2ed99b-285a-594d-9459-83bf84e2db1f",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Berry.Name",
    display_name="Berry",
    searchable_by=["Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=99,
    set_code="NEO1",
    rarity=Rarities.Common,
    granted_abilities=berry_between_turns("Berry", 20, 2)
)
