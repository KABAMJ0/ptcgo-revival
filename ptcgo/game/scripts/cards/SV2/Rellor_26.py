from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="943f1341-acf7-5b90-8918-43c00a0de55d",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rellor.Name",
    display_name="Rellor",
    searchable_by=["Rellor", "Basic", "Rellor"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=953,
    abilities=[
        Attack(
            title="Ball Roll",
            game_text="Flip a coin until you get tails. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(per_heads=30, until_tails=True),
        ),
    ],
)