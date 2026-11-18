from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import attacker_of_types, takes_less_from

card = PokemonToolCardDef(
    guid="1c19d36e-c7e3-51ac-8a80-4fe600bbc298",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OccaBerry.Name",
    display_name="Occa Berry",
    searchable_by=["Occa Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=140,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    passive=takes_less_from(60, None, attacker_of_types("fire"))
)
