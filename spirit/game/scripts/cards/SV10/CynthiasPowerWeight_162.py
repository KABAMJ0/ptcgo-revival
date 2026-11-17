from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import all_of, gated_hp_bonus, is_pokemon_card, owned_by

card = PokemonToolCardDef(
    guid="56e19ace-78e5-5789-a0a5-e04be86659b6",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiasPowerWeight.Name",
    display_name="Cynthia's Power Weight",
    searchable_by=["Cynthia's Power Weight", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=162,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    passive=gated_hp_bonus(70, all_of(is_pokemon_card, owned_by("cynthia")))
)
