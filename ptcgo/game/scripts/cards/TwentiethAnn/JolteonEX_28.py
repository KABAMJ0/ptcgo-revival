from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.passives_common import protect_next_turn, attacker_is_basic


card = PokemonCardDef(
    guid="6a9c12b9-c025-5f7f-9101-1b25ecce1679",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JolteonEX.Name",
    display_name="Jolteon-EX",
    searchable_by=["Jolteon-EX", "Basic", "EX", "JolteonEX"],
    subtypes=["Basic", "EX"],
    collector_number=28,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=135,
    abilities=[
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
        Attack(
            title="Flash Ray",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=protect_next_turn(prevent=True, attacker_pred=attacker_is_basic()),
        ),
    ],
)