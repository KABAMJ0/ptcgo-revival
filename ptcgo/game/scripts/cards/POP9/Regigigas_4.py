from ptcgo.game.card_effects.attacks_common import condition_attack, flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="5e9a41a0-aeaf-59d5-a567-c0b70f42043d",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    display_name="Regigigas",
    searchable_by=["Regigigas", "Basic", "Regigigas"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="POP9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Double Stomp",
            game_text="Flip 2 coins. This attack does 50 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            damage_operator="+",
            effect=flip_damage(coins=2, base=50, bonus_per_heads=20),
        ),
    ],
)