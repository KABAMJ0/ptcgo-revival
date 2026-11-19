from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.support_common import opponent_switches
from ptcgo.game.attributes import AttrID


def _defender_undamaged(ctx):
    defender = ctx.defender
    return defender is not None and defender.get_attribute(
        AttrID.HP, 0) >= ctx.max_hp(defender)


def _major_tsunami_available(board, player_id, pokemon):
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or not is_in_active_spot(pokemon):
        return False
    bench = board.find_player_area(player_id, "bench")
    if bench is not None and bench.children:
        return True
    return any(area.children for pid in board.player_ids if pid != player_id
               for area in [board.find_player_area(pid, "bench")] if area is not None)


async def _major_tsunami(ctx):
    if ctx.opponent_bench():
        await opponent_switches(ctx)
    bench = ctx.my_bench()
    if not bench:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="3c1d2607-2d12-5524-895f-e63ed2c2110c",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr",
    searchable_by=["Feraligatr", "Stage 2", "Feraligatr"],
    subtypes=["Stage 2"],
    collector_number=47,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Ability(
            title="Major Tsunami",
            game_text="Once during your turn (before your attack), if Feraligatr is your Active Pok\u00e9mon and if your opponent has any Benched Pok\u00e9mon, your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon. Either way, if you have any Benched Pok\u00e9mon, switch Feraligatr with 1 of them. This power can't be used if Feraligatr is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_major_tsunami_available,
            effect=_major_tsunami,
        ),
        Attack(
            title="Rending Jaws",
            game_text="If there are no damage counters on the Defending Pok\u00e9mon, this attack's base damage is 40 instead of 70.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=bonus_if(_defender_undamaged, -30, base=70),
        ),
    ],
)