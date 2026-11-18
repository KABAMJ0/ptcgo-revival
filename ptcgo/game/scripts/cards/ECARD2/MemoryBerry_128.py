from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import previous_evolution_grant_passive

card = PokemonToolCardDef(
    guid="9180b0d8-86ed-5a87-9d2d-5835854f425f",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MemoryBerry.Name",
    display_name="Memory Berry",
    searchable_by=["Memory Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=128,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    passive=previous_evolution_grant_passive()
)
