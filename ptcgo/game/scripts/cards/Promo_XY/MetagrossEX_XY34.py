from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import move_energy_between
from ptcgo.game.card_effects.pokemon import energy_provides_type

card = PokemonCardDef(
    guid="0b36186e-dd0c-5fe5-839e-9dcc6f5ed0ba",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MetagrossEX.Name",
    display_name="Metagross-EX",
    searchable_by=["Metagross-EX", "Basic", "EX", "MetagrossEX"],
    subtypes=["Basic", "EX"],
    collector_number=34,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=376,
    abilities=[
        Attack(
            title="Magnetic Laser",
            game_text="You may move a Metal Energy from 1 of your Benched Pok\u00e9mon to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=move_energy_between(predicate=lambda c: energy_provides_type(c, PokemonTypes.METAL.value), count=1, from_pool="bench", to_pool="active"),
        ),
        Attack(
            title="Squared Attack",
            game_text="Flip 4 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=50),
        ),
    ],
)