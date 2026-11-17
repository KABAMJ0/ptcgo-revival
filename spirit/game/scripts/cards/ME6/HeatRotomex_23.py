from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="adf51a2b-3c4d-510f-a20b-12b293068b73",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatRotomex.Name",
    display_name="Heat Rotom ex",
    searchable_by=["Heat Rotom ex", "Basic", "ex", "HeatRotomex"],
    subtypes=["Basic", "ex"],
    collector_number=23,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=479,
    abilities=[
        Attack(
            title="Rewarm",
            game_text="This attack does 30 damage for each Basic Fire Energy card in your discard pile. Then, shuffle those cards into your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Strong Flare",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=unimplemented,
        ),
    ],
)