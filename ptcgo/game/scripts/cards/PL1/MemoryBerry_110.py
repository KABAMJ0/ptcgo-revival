from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import previous_evolution_grant_passive

card = PokemonToolCardDef(
    guid="c794b28e-99eb-5f4a-954f-58d9ff0d5653",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MemoryBerry.Name",
    display_name="Memory Berry",
    searchable_by=["Memory Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=110,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    passive=previous_evolution_grant_passive()
)
