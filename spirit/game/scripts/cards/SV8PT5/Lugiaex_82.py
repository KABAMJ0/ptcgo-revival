from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bcefaffa-a561-50f1-9ed9-0897db73dbee",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugiaex.Name",
    display_name="Lugia ex",
    searchable_by=["Lugia ex", "Basic", "ex", "Lugiaex"],
    subtypes=["Basic", "ex"],
    collector_number=82,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Attack(
            title="Hyper Whirlpool",
            game_text="Flip a coin until you get tails. For each heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
            effect=unimplemented,
        ),
    ],
)