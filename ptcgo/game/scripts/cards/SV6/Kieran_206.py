from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, choose_one, is_pokemon_ex, is_pokemon_v_card, switch, turn_damage_boost_vs

card = SupporterCardDef(
    guid="b73637dd-3674-555a-a999-a2acb2549291",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kieran.Name",
    display_name="Kieran",
    searchable_by=["Kieran", "Supporter"],
    subtypes=["Supporter"],
    collector_number=206,
    set_code="SV6",
    rarity=Rarities.Rare,
    effect=choose_one([("Switch your Active Pokémon with 1 of your Benched Pokémon", switch), ("During this turn, attacks used by your Pokémon do 30 more damage to yo", turn_damage_boost_vs(30, any_of(is_pokemon_ex, is_pokemon_v_card)))])
)
