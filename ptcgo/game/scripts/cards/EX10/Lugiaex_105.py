from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="725ba406-1d90-5348-a74a-945e609b4c4a",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugiaex.Name",
    display_name="Lugia ex",
    searchable_by=["Lugia ex", "Basic", "ex", "Lugiaex"],
    subtypes=["Basic", "ex"],
    collector_number=105,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Ability(
            title="Silver Sparkle",
            game_text="If Lugia ex is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Lugia ex is Knocked Out), flip a coin. If heads, choose an Energy card attached to the Attacking Pok\u00e9mon and return it to your opponent's hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Elemental Blast",
            game_text="Discard a Fire Energy, Water Energy, and Lightning Energy attached to Lugia ex.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)