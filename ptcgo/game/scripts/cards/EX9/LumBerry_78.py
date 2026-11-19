from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import lum_berry_between_turns

card = PokemonToolCardDef(
    guid="a41af430-b9ee-54bc-abec-575b3842eb86",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LumBerry.Name",
    display_name="Lum Berry",
    searchable_by=["Lum Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=78,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    granted_abilities=lum_berry_between_turns("Lum Berry")
)
