from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="59914a0d-3d5f-5f39-81c3-e37843ca443e",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AshsPikachu.Name",
    display_name="Ash's Pikachu",
    searchable_by=["Ash's Pikachu", "Basic", "AshsPikachu"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=25,
    abilities=[
        Attack(
            title="Iron Tail",
            game_text="Flip a coin until you get tails. This attack does 20 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(per_heads=20, until_tails=True),
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)