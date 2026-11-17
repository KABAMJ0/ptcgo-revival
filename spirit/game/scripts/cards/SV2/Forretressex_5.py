from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5904b760-bf64-5ba0-a836-4e15f4654cf6",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretressex.Name",
    display_name="Forretress ex",
    searchable_by=["Forretress ex", "Stage 1", "Tera", "ex", "Forretressex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=5,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Ability(
            title="Exploding Energy",
            game_text="Once during your turn, you may search your deck for up to 5 Basic Grass Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck. If you searched your deck in this way, this Pok\u00e9mon is Knocked Out.",
            effect=unimplemented,
        ),
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)