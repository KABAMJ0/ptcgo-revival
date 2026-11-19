from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="202b1c6b-db7f-509e-ae90-4889087422d7",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1", "Magneton"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Tri Attack",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=20),
        ),
        Attack(
            title="Magnetic Ray",
            game_text="Before doing damage, you may choose 1 of your opponent's Benched Pok\u00e9mon that has any Energy attached to it and switch that Pok\u00e9mon with 1 of the Defending Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)