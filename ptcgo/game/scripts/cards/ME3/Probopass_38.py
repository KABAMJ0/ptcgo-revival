from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6a863681-999d-5bab-8bc4-52da40b9920d",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name",
    display_name="Probopass",
    searchable_by=["Probopass", "Stage 1", "Probopass"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="ME3",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    family_id=299,
    abilities=[
        Attack(
            title="Rolling Rocks",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
        ),
        Attack(
            title="Obliterating Nose",
            game_text="Discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=260,
            effect=unimplemented,
        ),
    ],
)