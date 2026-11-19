from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="726f929a-4fd5-57bc-b6dd-bfdc302e0130",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhanex.Name",
    display_name="Kangaskhan ex",
    searchable_by=["Kangaskhan ex", "Basic", "ex", "Kangaskhanex"],
    subtypes=["Basic", "ex"],
    collector_number=115,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=115,
    abilities=[
        Attack(
            title="Triple Draw",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(3),
        ),
        Attack(
            title="Incessant Punching",
            game_text="Flip 4 coins. This attack does 100 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=100),
        ),
    ],
)