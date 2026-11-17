from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="87f3b363-fac7-58e7-bf3d-330b639c005b",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squawkabilly.Name",
    display_name="Squawkabilly",
    searchable_by=["Squawkabilly", "Basic", "Squawkabilly"],
    subtypes=["Basic"],
    collector_number=141,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=931,
    abilities=[
        Attack(
            title="Add On",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)