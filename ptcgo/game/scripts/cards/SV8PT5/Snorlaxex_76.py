from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="79e3a114-d9b5-5404-b8a0-67605e0f6662",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlaxex.Name",
    display_name="Snorlax ex",
    searchable_by=["Snorlax ex", "Basic", "ex", "Snorlaxex"],
    subtypes=["Basic", "ex"],
    collector_number=76,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Attack(
            title="Strength",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
        Attack(
            title="Toss-and-Turn Press",
            game_text="Flip 3 coins. This attack does 120 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=120),
        ),
    ],
)