from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ea29d0d5-73c7-5c7d-85c5-d22cf39d41bd",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GyaradosEX.Name",
    display_name="Gyarados-EX",
    searchable_by=["Gyarados-EX", "Basic", "EX", "GyaradosEX"],
    subtypes=["Basic", "EX"],
    collector_number=106,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=130,
    abilities=[
        Attack(
            title="Stormy Seas",
            game_text="Flips a coin until you get tails. For each heads, search your deck for a Water Energy card and attach it to this Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Splash Burn",
            game_text="This attack does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=spread_damage(10, side="mine", also_base=True),
        ),
    ],
)