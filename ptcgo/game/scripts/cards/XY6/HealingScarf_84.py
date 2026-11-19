from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import healing_scarf_energy_attach

card = PokemonToolCardDef(
    guid="3afe7f14-cec5-5487-b190-e53ffd5fbfa2",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HealingScarf.Name",
    display_name="Healing Scarf",
    searchable_by=["Healing Scarf", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=84,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    granted_abilities=healing_scarf_energy_attach('Healing Scarf', 20),
)
