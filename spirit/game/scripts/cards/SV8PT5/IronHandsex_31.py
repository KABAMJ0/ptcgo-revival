from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="af9f32b8-891c-5c91-8168-2ff26c574383",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronHandsex.Name",
    display_name="Iron Hands ex",
    searchable_by=["Iron Hands ex", "Basic", "ex", "Future", "IronHandsex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=31,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Arm Press",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
        Attack(
            title="Amp You Very Much",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)