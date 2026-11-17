from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0c0005bf-5a5b-5eee-98e3-41b1ccd00256",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotomex.Name",
    display_name="Rotom ex",
    searchable_by=["Rotom ex", "Basic", "ex", "Rotomex"],
    subtypes=["Basic", "ex"],
    collector_number=111,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Ability(
            title="Multi Adapter",
            game_text="Each of your Pok\u00e9mon that has \"Rotom\" in its name may have up to 2 Pok\u00e9mon Tool cards attached. If this Ability goes away, discard Pok\u00e9mon Tools from those Pok\u00e9mon until only 1 remains on each.",
            effect=unimplemented,
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)