from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="937715cc-d299-5b20-9584-a1d97d95c5cb",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhGX.Name",
    display_name="Ho-Oh-GX",
    searchable_by=["Ho-Oh-GX", "Basic", "GX", "HoOhGX"],
    subtypes=["Basic", "GX"],
    collector_number=50,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Attack(
            title="Sacred Fire",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Phoenix Burn",
            game_text="This Pok\u00e9mon can't use Phoenix Burn during your next turn.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=unimplemented,
        ),
        Attack(
            title="Eternal Light-GX",
            game_text="Put 3 in any combination of Fire Pok\u00e9mon-GX or Fire Pok\u00e9mon-EX from your discard pile onto your Bench. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)