from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="baf5f95f-95b3-5370-9604-cd747945ae17",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name",
    display_name="Unown [!]",
    searchable_by=["Unown [!]", "Basic", "Unown"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="!",
            game_text="Once during your turn, when you put Unown ! from your hand onto your Bench, you may flip a coin. If heads, put 2 damage counters on 1 of your opponent's Pok\u00e9mon. If tails, put 2 damage counters on 1 of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage. If tails, Unown ! does 10 damage to itself, and this attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)