from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="14de2b62-9629-5e23-85d1-20e564c8577b",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    display_name="Tangela",
    searchable_by=["Tangela", "Basic", "Tangela"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=114,
    abilities=[
        Attack(
            title="Tickling Vines",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Double Kick",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
    ],
)