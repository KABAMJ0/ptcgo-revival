from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, flip_damage
from ptcgo.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="e9dd8f19-3486-5dcc-a02f-c1da284a4bc2",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name",
    display_name="Volcanion",
    searchable_by=["Volcanion", "Basic", "Volcanion"],
    subtypes=["Basic"],
    collector_number=164,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Attack(
            title="Concentrated Fire",
            game_text="Flip a coin for each Fire Energy attached to this Pok\u00e9mon. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins_from=count_energy("self", PokemonTypes.FIRE), per_heads=50),
        ),
        Attack(
            title="Combustion Impact",
            game_text="Your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)