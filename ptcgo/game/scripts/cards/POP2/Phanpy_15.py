from ptcgo.game.card_effects.attacks_common import flip_damage, condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="b69cb2b5-d87b-5e61-8915-369464cceefe",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    display_name="Phanpy",
    searchable_by=["Phanpy", "Basic", "Phanpy"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="POP2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=231,
    abilities=[
        Attack(
            title="Double Spin",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=10),
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)