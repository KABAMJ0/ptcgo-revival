from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import attacker_has_subtypes, excluding, pokemon_of_subtype, takes_less_from

card = PokemonToolCardDef(
    guid="0f147bd5-e376-53c5-aed3-f7f6b7c66be3",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CustomVest.Name",
    display_name="Custom Vest",
    searchable_by=["Custom Vest", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=127,
    set_code="ME6",
    rarity=Rarities.Rare,
    passive=takes_less_from(60, excluding(pokemon_of_subtype("MEGA")), attacker_has_subtypes("MEGA", "ex"))
)
