from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.session.passives import Passive


class MirrorShellPassive(Passive):
    """The damage an attack lands on Dark Wartortle is bounced back onto the
    attacking Pokemon, an equal amount and unmodified."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if target is not carrier:
            return None
        if calc.attacker is not None:
            await ctx.deal_damage(calc.amount, target=calc.attacker,
                                  apply_modifiers=False)
        return None


async def mirror_shell(ctx):
    ctx.add_passive_through_opponents_turn(ctx.attacker, MirrorShellPassive())

card = PokemonCardDef(
    guid="4134c2ce-6309-5de2-b695-3d2d80c5d07a",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkWartortle.Name",
    display_name="Dark Wartortle",
    searchable_by=["Dark Wartortle", "Stage 1", "DarkWartortle"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    family_id=7,
    abilities=[
        Attack(
            title="Doubleslap",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=10),
        ),
        Attack(
            title="Mirror Shell",
            game_text="If an attack does damage to Dark Wartortle during your opponent's next turn (even if Dark Wartortle is Knocked Out), Dark Wartortle attacks the Defending Pok\u00e9mon for an equal amount of damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=mirror_shell,
        ),
    ],
)