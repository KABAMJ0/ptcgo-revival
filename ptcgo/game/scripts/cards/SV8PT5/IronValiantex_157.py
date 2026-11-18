from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e27bfaa4-932d-52bd-bf16-36b79338bbcb",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronValiantex.Name",
    display_name="Iron Valiant ex",
    searchable_by=["Iron Valiant ex", "Basic", "ex", "Future", "IronValiantex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=157,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    abilities=[
        Ability(
            title="Tachyon Bits",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to the Active Spot, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Laser Blade",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)