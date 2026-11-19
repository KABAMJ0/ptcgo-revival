from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="81d1f60b-2c5c-5c2e-a0d9-b45cc299935e",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysCloyster.Name",
    display_name="Misty's Cloyster",
    searchable_by=["Misty's Cloyster", "Stage 1", "MistysCloyster"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysShellder.Name",
    family_id=90,
    abilities=[
        Ability(
            title="Shell Armor",
            game_text="You may reduce all damage done by attacks to Misty's Cloyster by 10 (after applying Weakness and Resistance). (Any other effects of attacks still happen). This power can't be used if Misty's Cloyster is Asleep, Confused, or Paralyzed.",
            effect=unimplemented,
        ),
        Attack(
            title="Triple Cannon",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=20),
        ),
    ],
)