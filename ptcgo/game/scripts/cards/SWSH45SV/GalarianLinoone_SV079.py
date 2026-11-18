from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ce0589e1-3d95-5426-a720-e00a83162c9a",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianLinoone.Name",
    display_name="Galarian Linoone",
    searchable_by=["Galarian Linoone", "Stage 1", "GalarianLinoone"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZigzagoon.Name",
    family_id=263,
    abilities=[
        Attack(
            title="Night Slash",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)