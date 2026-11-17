from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import attacker_has_subtypes, excluding, pokemon_of_subtype, takes_less_from

card = PokemonToolCardDef(
    guid="eeeda4d1-3dcd-5073-907f-fee0c085555c",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CustomVest.Name",
    display_name="Custom Vest",
    searchable_by=["Custom Vest", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=91,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    passive=takes_less_from(60, excluding(pokemon_of_subtype("MEGA")), attacker_has_subtypes("MEGA", "ex"))
)
