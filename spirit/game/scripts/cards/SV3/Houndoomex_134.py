from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e4baa71a-654c-5f08-bec8-783eb80913e4",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoomex.Name",
    display_name="Houndoom ex",
    searchable_by=["Houndoom ex", "Stage 1", "ex", "Houndoomex"],
    subtypes=["Stage 1", "ex"],
    collector_number=134,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Evil Claw",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=90,
            effect=unimplemented,
        ),
        Attack(
            title="Hound's Fang",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=220,
            effect=unimplemented,
        ),
    ],
)