from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.pokemon import is_psychic_energy
from ptcgo.game.card_effects.passives_common import Passive, carrier_pokemon


class _DestinyBond(Passive):
    """During the opponent's next turn, the attacker that KOs Froslass is
    Knocked Out too."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if carrier_pokemon(carrier) is not target:
            return None
        if calc.amount < target.get_attribute(AttrID.HP, 0):
            return None
        attacker = calc.attacker
        if attacker is None or attacker.owning_player_id == target.owning_player_id:
            return None

        await ctx.knock_out(attacker)
        return None


async def _destiny_bond(ctx):
    await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=is_psychic_energy,
        prompt="Discard a Psychic Energy attached to Froslass")
    if ctx.attacker is not None:
        ctx.add_passive_through_opponents_turn(ctx.attacker, _DestinyBond())


async def _icy_breath_bench(ctx):
    for pokemon in ctx.opponent_bench():
        await ctx.deal_damage(10, target=pokemon, as_counters=True)


card = PokemonCardDef(
    guid="d0aaf05b-c68f-517d-aa73-8a5d1ab760a9",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froslass.Name",
    display_name="Froslass",
    searchable_by=["Froslass", "Stage 1", "Froslass"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=478,
    abilities=[
        Attack(
            title="Destiny Bond",
            game_text="Discard a Psychic Energy attached to Froslass. During your opponent's next turn, if Froslass would be Knocked Out by damage from an attack, the Attacking Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_destiny_bond,
        ),
        Attack(
            title="Icy Breath",
            game_text="The Defending Pok\u00e9mon is now Asleep. Put 1 damage counter on each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=condition_attack(SpecialConditions.ASLEEP, also=_icy_breath_bench),
        ),
    ],
)