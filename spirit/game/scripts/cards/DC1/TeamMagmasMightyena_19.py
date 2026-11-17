from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eef5f798-74c3-54bf-a655-55137ba8b5ad",
    key="DC1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasMightyena.Name",
    display_name="Team Magma's Mightyena",
    searchable_by=["Team Magma's Mightyena", "Stage 1", "TeamMagmasMightyena"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="DC1",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasPoochyena.Name",
    family_id=261,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Hostile Fang",
            game_text="If your opponent's Active Pok\u00e9mon is a Team Aqua Pok\u00e9mon, this attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)