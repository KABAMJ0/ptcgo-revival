from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID
from ptcgo.game.session.passives import effective_max_hp
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.session.effects import is_trainer_card
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _has_damage_counters(board, player_id, pokemon):
    active = board.active_pokemon(player_id)
    return active is not None \
        and active.get_attribute(AttrID.HP, 0) < effective_max_hp(board, active)


async def spacing_out(ctx):
    """Flip a coin. If heads, remove a damage counter from Slowpoke."""
    active = ctx.attacker
    if active is None:
        return
    heads = await ctx.flip_coins(1, ctx.ability.title)
    if heads and heads[0]:
        await ctx.heal(10, active)


_is_psychic_energy = basic_energy_of("psychic")


def _can_scavenge(board, player_id, pokemon):
    """The attack needs a Psychic Energy on Slowpoke to pay its discard cost."""
    active = board.active_pokemon(player_id)
    return active is not None \
        and any(_is_psychic_energy(card) for card in board.attached_energies(active))


async def scavenge(ctx):
    """Discard a Psychic Energy from Slowpoke, then take a Trainer card out of
    the discard pile."""
    attacker = ctx.attacker
    if attacker is None:
        return
    if not any(_is_psychic_energy(card) for card in ctx.attached_energies(attacker)):
        return
    await ctx.discard_energy_from(
        attacker, 1, predicate=_is_psychic_energy,
        prompt="Discard a Psychic Energy from Slowpoke")
    await recover_from_discard(is_trainer_card, count=1, minimum=1,
                               prompt="Choose a Trainer card")(ctx)


card = PokemonCardDef(
    guid="3566b3d2-d2cb-5f83-ad15-d4c5f3866b28",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="BASE6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=79,
    abilities=[
        Attack(
            title="Spacing Out",
            game_text="Flip a coin. If heads, remove a damage counter from Slowpoke. This attack can't be used if Slowpoke has no damage counters on it.",
            cost={PokemonTypes.COLORLESS: 1},
            condition=_has_damage_counters,
            effect=spacing_out,
        ),
        Attack(
            title="Scavenge",
            game_text="Discard 1 Psychic Energy card attached to Slowpoke in order to use this attack. Put a Trainer card from your discard pile into your hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            condition=_can_scavenge,
            effect=scavenge,
        ),
    ],
)