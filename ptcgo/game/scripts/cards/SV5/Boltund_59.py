from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c4c755a5-712e-5985-9717-d6c4aa1b21f2",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Boltund.Name",
    display_name="Boltund",
    searchable_by=["Boltund", "Stage 1", "Boltund"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamper.Name",
    family_id=835,
    abilities=[
        Attack(
            title="Electrifying Dash",
            game_text="Search your deck for up to 2 Basic Lightning Energy cards and attach them to your Benched Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)