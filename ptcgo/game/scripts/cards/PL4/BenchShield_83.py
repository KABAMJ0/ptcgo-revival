from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import benched_full_shield_passive


card = PokemonToolCardDef(
    guid="853c3710-b026-5148-bbc5-eb4bdf9d7fa7",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BenchShield.Name",
    display_name="Bench Shield",
    searchable_by=["Bench Shield", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=83,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    passive=benched_full_shield_passive(),
)
