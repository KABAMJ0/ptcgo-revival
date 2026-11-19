from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import RetaliateCountersPassive, Passive
from ptcgo.game.data_utils import def_for
from ptcgo.game.session.passives import carrier_pokemon


def _bench_count(board, player_id) -> int:
    area = board.find_player_area(player_id, "bench")
    return len(getattr(area, "children", []) or [])


def _other_player(board, player_id):
    return next(pid for pid in (getattr(board, "player_ids", None) or [])
                if pid != player_id)


class _RevengeFang(Passive):
    """+40 to the Active while Houndoom's owner has fewer Benched Pokemon."""

    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        if not (calc.is_attack and calc.is_opposing and attacker is not None):
            return
        if attacker is not carrier_pokemon(carrier) or not calc.to_active:
            return
        mine = _bench_count(calc.board, carrier.owning_player_id)
        theirs = _bench_count(calc.board, _other_player(calc.board, carrier.owning_player_id))
        if mine < theirs:
            calc.amount += 40

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
            effect=unimplemented,
        ),
        Attack(
            title="Bright Flame",
            game_text="Flip a coin. If tails, discard 2 Fire Energy attached to Houndoom.",
            cost={PokemonTypes.FIRE: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)