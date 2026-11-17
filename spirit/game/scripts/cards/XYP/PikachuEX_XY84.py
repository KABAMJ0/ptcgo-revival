from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c8d3348f-6acc-51a2-a039-04ec2a651617",
    key="XYP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuEX.Name",
    display_name="Pikachu-EX",
    searchable_by=["Pikachu-EX", "Basic", "EX", "PikachuEX"],
    subtypes=["Basic", "EX"],
    collector_number=84,
    set_code="XYP",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=25,
    abilities=[
        Attack(
            title="Iron Tail",
            game_text="Flip a coin until you get tails. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Overspark",
            game_text="Discard all Lightning Energy attached to this Pok\u00e9mon. This attack does 50 damage times the number of Energy cards you discarded.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)