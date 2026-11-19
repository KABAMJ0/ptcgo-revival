from ptcgo.game.card_effects.attacks_common import flip_damage_condition
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="5eb06577-f31b-5cf8-8b2d-1e26b0038915",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name",
    display_name="Vanilluxe",
    searchable_by=["Vanilluxe", "Stage 2", "Vanilluxe"],
    subtypes=["Stage 2"],
    collector_number=29,
    set_code="RSV10PT5",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Double Freeze",
            game_text="Flip 2 coins. This attack does 90 damage for each heads. If either of them is heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="x",
            effect=flip_damage_condition(2, per_heads=90, min_heads=1, condition=SpecialConditions.PARALYZED),
        ),
    ],
)