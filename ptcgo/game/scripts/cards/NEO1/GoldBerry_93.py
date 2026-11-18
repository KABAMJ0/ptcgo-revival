from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import berry_between_turns

card = PokemonToolCardDef(
    guid="5f5d9d4e-476f-56a0-8e63-c53791a6a19c",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GoldBerry.Name",
    display_name="Gold Berry",
    searchable_by=["Gold Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=93,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    granted_abilities=berry_between_turns("Gold Berry", 40, 4)
)
