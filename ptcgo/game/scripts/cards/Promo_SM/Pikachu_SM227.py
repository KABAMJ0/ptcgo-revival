from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9bde85de-f865-53e2-be40-69134efa8ebe",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=227,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=25,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)