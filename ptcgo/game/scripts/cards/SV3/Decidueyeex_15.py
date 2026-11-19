from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _total_freedom(ctx):
    bench = ctx.my_bench()
    if ctx.source is ctx.my_active():
        if not bench:
            return
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose your new Active Pok\u00e9mon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    elif ctx.my_active() is not None:
        await ctx.switch_active(ctx.player_id, ctx.source)


def _total_freedom_offered(board, player_id, pokemon):
    active = board.active_pokemon(player_id)
    bench = board.find_player_area(player_id, "bench")
    on_bench = any(child is pokemon for child in (bench.children if bench else []))
    if active is pokemon:
        return bool(bench and bench.children)
    if on_bench:
        return active is not None
    return False


card = PokemonCardDef(
    guid="a52358c3-dbd3-51ef-b34c-f083f2a2e569",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Decidueyeex.Name",
    display_name="Decidueye ex",
    searchable_by=["Decidueye ex", "Stage 2", "ex", "Decidueyeex"],
    subtypes=["Stage 2", "ex"],
    collector_number=15,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=722,
    abilities=[
        Ability(
            title="Total Freedom",
            game_text="Once during your turn, you may use this Ability. If this Pok\u00e9mon is on the Bench, switch it with your Active Pok\u00e9mon. Or, if this Pok\u00e9mon is in the Active Spot, switch it with 1 of your Benched Pok\u00e9mon.",
            effect=_total_freedom,
            activation=Activations.ONCE_PER_TURN,
            condition=_total_freedom_offered,
        ),
        Attack(
            title="Hunting Arrow",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=snipe_attack(30, pool="bench", count=1, apply_modifiers=False, also_base=True),
        ),
    ],
)
