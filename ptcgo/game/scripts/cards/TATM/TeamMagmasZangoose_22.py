from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.trainers import all_of, named

card = PokemonCardDef(
    guid="832fc007-ff56-594b-9af7-f7b47447eabd",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasZangoose.Name",
    display_name="Team Magma's Zangoose",
    searchable_by=["Team Magma's Zangoose", "Basic", "TeamMagmasZangoose"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="TATM",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Team Magma Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(all_of(is_basic_pokemon, named("team magma")), count=2),
        ),
        Attack(
            title="Team Play",
            game_text="This attack does 20 damage times the number of Team Magma Pok\u00e9mon on your Bench.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)