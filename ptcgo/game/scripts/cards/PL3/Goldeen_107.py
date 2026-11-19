from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0b6cbc08-b5f8-5cfb-b500-cf420975488d",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goldeen.Name",
    display_name="Goldeen",
    searchable_by=["Goldeen", "Basic", "Goldeen"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="PL3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=118,
    abilities=[
        Attack(
            title="Flail",
            game_text="Does 10 damage times the number of damage counters on Goldeen.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Fury Attack",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=10),
        ),
    ],
)