from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="20a3a68e-3396-5057-844a-96abb5f1fc21",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompC.Name",
    display_name="Garchomp C",
    searchable_by=["Garchomp C", "Basic", "SP", "GarchompC"],
    subtypes=["Basic", "SP"],
    collector_number=60,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    family_id=445,
    abilities=[
        Attack(
            title="Claw Swipe",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Earthquake",
            game_text="This attack does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=spread_damage(10, side="mine", also_base=True),
        ),
    ],
)