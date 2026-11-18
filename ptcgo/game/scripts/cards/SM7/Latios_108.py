from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per, count_in_play
from ptcgo.game.card_effects.trainers import all_of, pokemon_of
from ptcgo.game.session.effects import is_evolution_pokemon

card = PokemonCardDef(
    guid="88fd5ede-5c1c-5fc3-a4e4-e0e59433567b",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios ◇",
    searchable_by=["Latios \u25c7", "Basic", "Prism Star", "Latios"],
    subtypes=["Basic", "Prism Star"],
    collector_number=108,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=381,
    abilities=[
        Attack(
            title="Dragon Fleet",
            game_text="This attack does 50 damage for each of your Evolution Dragon Pok\u00e9mon in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_in_play("mine", all_of(pokemon_of("dragon"), is_evolution_pokemon)), 50),
        ),
    ],
)