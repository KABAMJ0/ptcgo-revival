from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="bc2312dd-0f61-50aa-a5bd-e40980767cc1",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    display_name="Lugia",
    searchable_by=["Lugia", "Basic", "Lugia"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Aeroblast",
            game_text="Flip 2 coins. This attack does 50 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_damage(coins=2, base=50, bonus_per_heads=20),
        ),
    ],
)