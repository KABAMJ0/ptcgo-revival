from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import attacker_of_types, takes_less_from

card = PokemonToolCardDef(
    guid="44960f9e-3b9b-5016-9c05-9534dfd80a1a",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BabiriBerry.Name",
    display_name="Babiri Berry",
    searchable_by=["Babiri Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=163,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    passive=takes_less_from(60, None, attacker_of_types("metal"))
)
