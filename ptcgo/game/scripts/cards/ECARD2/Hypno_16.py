from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.attributes import SpecialConditions, AttrID


def _sleep_pendulum_available(board, player_id, pokemon):
    if not is_in_active_spot(pokemon) or pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    opponent_id = next((pid for pid in board.player_ids if pid != player_id), None)
    active = board.active_pokemon(opponent_id) if opponent_id else None
    if active is None:
        return False
    return not active.get_attribute(AttrID.SPECIAL_CONDITIONS)


async def _sleep_pendulum(ctx):
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)


async def _spiral_aura(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or defender.get_attribute(AttrID.HP, 0) <= 0:
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    if not await ctx.ask_yes_no("Switch the Defending Pokémon with a Benched Pokémon?"):
        return
    target = await ctx.choose_pokemon(bench, "Choose the opponent's new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


card = PokemonCardDef(
    guid="1d9881f2-d3cb-5fd4-bd7d-18c14f7b324f",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1", "Hypno"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Ability(
            title="Sleep Pendulum",
            game_text="Once during your turn (before your attack), if Hypno is your Active Pok\u00e9mon, you may make the Defending Pok\u00e9mon Asleep. This power can't be used if Hypno is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_sleep_pendulum_available,
            effect=_sleep_pendulum,
        ),
        Attack(
            title="Spiral Aura",
            game_text="If the Defending Pok\u00e9mon isn't Knocked Out by the damage from this attack, you may choose 1 of your opponent's Benched Pok\u00e9mon and switch the Defending Pok\u00e9mon with it.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_spiral_aura,
        ),
    ],
)