from ptcgo.game.card_effects.attacks_common import flip_damage, condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="065e385d-3cfc-57e3-97dc-086e888007b0",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    display_name="Bagon",
    searchable_by=["Bagon", "Basic", "Bagon"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="EX8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIRE,
    family_id=371,
    abilities=[
        Attack(
            title="Singe",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=condition_attack(SpecialConditions.BURNED, flip=True),
        ),
        Attack(
            title="Doubleslap",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=10),
        ),
    ],
)