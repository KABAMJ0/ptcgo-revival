from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9b46a198-65a5-59e3-862b-14907056269d",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownE.Name",
    display_name="Unown [E]",
    searchable_by=["Unown [E]", "Basic", "UnownE"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="EQUIP",
            game_text="Once during your turn (before your attack), if Unown E is on your Bench, you may discard all cards attached to Unown E and attach Unown E to 1 of your Pok\u00e9mon as a Pok\u00e9mon Tool card. As long as Unown E is attached to a Pok\u00e9mon, that Pok\u00e9mon gets +10 HP.",
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="During your opponent's next turn, whenever your opponent flips a coin, treat it as tails.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)