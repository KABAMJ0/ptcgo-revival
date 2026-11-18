from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f37e9b3c-677b-55db-903f-b02aef3885fe",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MMewtwoEX.Name",
    display_name="M Mewtwo-EX",
    searchable_by=["M Mewtwo-EX", "MEGA", "EX", "MMewtwoEX"],
    subtypes=["MEGA", "EX"],
    collector_number=160,
    set_code="XY8",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name",
    family_id=150,
    abilities=[
        Attack(
            title="Psychic Infinity",
            game_text="This attack does 30 more damage times the amount of Energy attached to both Active Pok\u00e9mon. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)