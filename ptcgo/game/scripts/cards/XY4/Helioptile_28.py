from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2fb4b20a-2efc-5a6c-87c4-b6269afb9169",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    display_name="Helioptile",
    searchable_by=["Helioptile", "Basic", "Helioptile"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="XY4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=694,
    abilities=[
        Attack(
            title="Tail Rap",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
    ],
)