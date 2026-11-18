from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="a80ed4e5-9ac9-53bb-b79a-b6509e23277c",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    display_name="Capsakid",
    searchable_by=["Capsakid", "Basic", "Capsakid"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=951,
    abilities=[
        Attack(
            title="Double Headbutt",
            game_text="Flip 2 coins. This attack does 50 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=50),
        ),
    ],
)