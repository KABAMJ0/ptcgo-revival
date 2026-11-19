from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="660a86fa-b3cf-5a11-8443-b7c3b9e1a7a2",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.YanmegaE4.Name",
    display_name="Yanmega E4",
    searchable_by=["Yanmega E4", "Basic", "SP", "YanmegaE4"],
    subtypes=["Basic", "SP"],
    collector_number=37,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=469,
    abilities=[
        Attack(
            title="Skill Dive",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(10, pool="any"),
        ),
        Attack(
            title="Whirlwind",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)