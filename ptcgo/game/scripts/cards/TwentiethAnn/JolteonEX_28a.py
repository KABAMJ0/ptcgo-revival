from ptcgo.game.card_effects.passives_common import prevent_damage_when
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

async def _max_balloon(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(
        ctx.attacker, prevent_damage_when(_max_balloon_shield)
    )


def _max_balloon_shield(calc, carrier):
    if calc.target is not carrier:
        return False
    attacker = calc.attacker
    return attacker is not None and \
        attacker.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value

card = PokemonCardDef(
    guid="decd5fd4-92b6-5f8f-9a14-88d121cbb7c6",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JolteonEX.Name",
    display_name="Jolteon-EX",
    searchable_by=["Jolteon-EX", "Basic", "EX", "JolteonEX"],
    subtypes=["Basic", "EX"],
    collector_number=28,
    set_code="TwentiethAnn",
    rarity=Rarities.RareUltra,
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
            effect=_max_balloon,
        ),
    ],
)