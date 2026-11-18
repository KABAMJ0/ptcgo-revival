from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b4ce5441-5dea-56da-a96b-3362eb80c6f8",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name",
    display_name="Steenee",
    searchable_by=["Steenee", "Stage 1", "Steenee"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bounsweet.Name",
    family_id=761,
    abilities=[
        Attack(
            title="Aromatherapy",
            game_text="Heal 30 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 2},
            damage=60,
        ),
    ],
)