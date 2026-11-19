from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import conditions_if, has_damage
from ptcgo.game.card_effects.pokemon import is_fire_energy
from ptcgo.game.card_effects.passives_common import Passive, carrier_pokemon


def _bench_count(board, player_id):
    active = board.active_pokemon(player_id)
    return sum(1 for pokemon in board.pokemon_in_play(player_id) if pokemon is not active)


class _RevengeFang(Passive):
    """+40 to Houndoom's attacks on the Active while it has fewer Benched."""

    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        if not (calc.is_attack and calc.is_opposing and attacker is not None):
            return
        if carrier_pokemon(carrier) is not attacker or not calc.to_active:
            return
        owner = attacker.owning_player_id
        opponent = next(pid for pid in calc.board.player_ids if pid != owner)
        if _bench_count(calc.board, owner) < _bench_count(calc.board, opponent):
            calc.amount += 40


async def _bright_flame(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Bright Flame")
    if not (results and results[0]):
        await ctx.discard_energy_from(
            ctx.attacker, 2, predicate=is_fire_energy,
            prompt="Discard 2 Fire Energy attached to Houndoom")


card = PokemonCardDef(
    guid="13aa6d13-62b6-5b6d-99cc-cd127aaa1b81",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Houndoom"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Ability(
            title="Revenge Fang",
            game_text="If you have less Benched Pok\u00e9mon than your opponent, each of Houndoom's attacks does 40 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=_RevengeFang(),
        ),
        Attack(
            title="Burning Sensation",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=conditions_if(has_damage("defender"), SpecialConditions.BURNED),
        ),
        Attack(
            title="Bright Flame",
            game_text="Flip a coin. If tails, discard 2 Fire Energy attached to Houndoom.",
            cost={PokemonTypes.FIRE: 2},
            damage=60,
            effect=_bright_flame,
        ),
    ],
)