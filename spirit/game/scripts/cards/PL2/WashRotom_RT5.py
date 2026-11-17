from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="307dfd61-9e1d-5125-8da0-1c881801eef5",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WashRotom.Name",
    display_name="Wash Rotom",
    searchable_by=["Wash Rotom", "Basic", "WashRotom"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=479,
    abilities=[
        Ability(
            title="Wash Shift",
            game_text="Once during your turn (before your attack), you may use this power. Wash Rotom's type is Water until the end of your turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Cleanse Away",
            game_text="Remove 3 damage counters from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Drain Wash",
            game_text="Flip a coin until you get tails. For each heads, choose 1 card from your opponent's hand without looking and discard it.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)