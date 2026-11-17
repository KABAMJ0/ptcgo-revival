from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import any_of, choose_one, is_pokemon_ex, is_pokemon_v_card, switch, turn_damage_boost_vs

card = SupporterCardDef(
    guid="7112c12d-bb2b-5338-b334-204e4da4a459",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kieran.Name",
    display_name="Kieran",
    searchable_by=["Kieran", "Supporter"],
    subtypes=["Supporter"],
    collector_number=113,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    effect=choose_one([("Switch your Active Pokémon with 1 of your Benched Pokémon", switch), ("During this turn, attacks used by your Pokémon do 30 more damage to yo", turn_damage_boost_vs(30, any_of(is_pokemon_ex, is_pokemon_v_card)))])
)
