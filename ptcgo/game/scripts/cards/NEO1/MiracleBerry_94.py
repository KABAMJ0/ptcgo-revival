from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import lum_berry_between_turns

card = PokemonToolCardDef(
    guid="a31fc863-83ce-58d4-a71d-8799b86444a3",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiracleBerry.Name",
    display_name="Miracle Berry",
    searchable_by=["Miracle Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=94,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    granted_abilities=lum_berry_between_turns("Miracle Berry")
)
