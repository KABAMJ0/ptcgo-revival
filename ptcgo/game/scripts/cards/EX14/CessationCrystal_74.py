from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import cessation_crystal_tool, cessation_crystal_attach_to

card = PokemonToolCardDef(
    guid="bb431f97-354d-50ef-861f-38d9c248a1e2",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CessationCrystal.Name",
    display_name="Cessation Crystal",
    searchable_by=["Cessation Crystal", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=74,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    passive=cessation_crystal_tool(),
    attach_to=cessation_crystal_attach_to,
)
