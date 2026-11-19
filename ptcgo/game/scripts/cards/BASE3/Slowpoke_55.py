from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_psychic_energy_card
from ptcgo.game.session.effects import is_trainer_card
from ptcgo.game.session.passives import effective_max_hp


def _has_damage(board, player_id, pokemon):
    return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


def _can_scavenge(board, player_id, pokemon):
    attached = any(is_psychic_energy_card(e)
                   for e in board.attached_energies(pokemon))
    return attached and any(is_trainer_card(c) for c in board.find_player_area(
        player_id, "discard").children)


async def _spacing_out(ctx):
    """Flip a coin; heads removes a damage counter from this Pokemon."""
    heads = await ctx.flip_coins(1, "Spacing Out")
    if heads and heads[0]:
        await ctx.heal(10, ctx.attacker)


async def _scavenge(ctx):
    """Discard a Psychic Energy attached to this Pokemon; if you do, put a
    Trainer card from your discard pile into your hand."""
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=is_psychic_energy_card,
        prompt="Choose a Psychic Energy to discard from this Pokemon")
    if not discarded:
        return
    await recover_from_discard(is_trainer_card, count=1)(ctx)

card = PokemonCardDef(
    guid="2ed3486f-46bb-5f11-a1b4-d319b8e07550",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="BASE3",
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
            condition=_has_damage,
            effect=_spacing_out,
        ),
        Attack(
            title="Scavenge",
            game_text="Discard 1 Psychic Energy card attached to Slowpoke in order to use this attack. Put a Trainer card from your discard pile into your hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            condition=_can_scavenge,
            effect=_scavenge,
        ),
    ],
)