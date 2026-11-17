from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import combined, gated_hp_bonus, holder_prize_shift, is_rule_box_free_pokemon

card = PokemonToolCardDef(
    guid="bcdf471d-5f95-5b66-9cc9-bcd7d0f57b00",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuxuriousCape.Name",
    display_name="Luxurious Cape",
    searchable_by=["Luxurious Cape", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=166,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    passive=combined(gated_hp_bonus(100, is_rule_box_free_pokemon), holder_prize_shift(1, is_rule_box_free_pokemon))
)
