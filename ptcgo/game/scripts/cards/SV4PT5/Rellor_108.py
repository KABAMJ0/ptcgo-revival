from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d03b0e0a-f5a6-516e-890f-40b029b5233a",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rellor.Name",
    display_name="Rellor",
    searchable_by=["Rellor", "Basic", "Rellor"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
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