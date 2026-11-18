from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="65412127-c744-5c9b-a787-677940272fc4",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasPoochyena.Name",
    display_name="Team Aqua's Poochyena",
    searchable_by=["Team Aqua's Poochyena", "Basic", "TeamAquasPoochyena"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=261,
    abilities=[
        Attack(
            title="Double Scratch",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Tail Slap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)