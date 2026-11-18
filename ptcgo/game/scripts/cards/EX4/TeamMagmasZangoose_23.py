from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.patterns import is_pokemon_of_type
from ptcgo.game.card_effects.trainers import all_of, any_of, named

card = PokemonCardDef(
    guid="2680f85b-01db-5074-acca-164640d7bee2",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasZangoose.Name",
    display_name="Team Magma's Zangoose",
    searchable_by=["Team Magma's Zangoose", "Basic", "TeamMagmasZangoose"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="EX4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Colorless Basic Pok\u00e9mon or Basic Pok\u00e9mon with Team Magma in its name and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(any_of(all_of(is_basic_pokemon, lambda card: is_pokemon_of_type(card, "colorless")), all_of(is_basic_pokemon, named("team magma"))), count=1),
        ),
        Attack(
            title="Team Play",
            game_text="Does 10 damage times the number of Pok\u00e9mon in play with Team Magma in its name.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)