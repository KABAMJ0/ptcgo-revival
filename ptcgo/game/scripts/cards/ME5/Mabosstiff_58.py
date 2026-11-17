from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bad124fc-0e25-57c6-8f8e-740fd3350d08",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mabosstiff.Name",
    display_name="Mabosstiff",
    searchable_by=["Mabosstiff", "Stage 1", "Mabosstiff"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name",
    family_id=942,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
        ),
        Attack(
            title="Plunging Headbutt",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 100 more damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 3},
            damage=210,
            effect=unimplemented,
        ),
    ],
)