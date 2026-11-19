from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import AttrID, TrainerType
from ptcgo.game.session.effects import resolve_trainer_effect


def _is_supporter(card):
    return (card.get_attribute(AttrID.CARD_TYPE) == 2
            and card.get_attribute(AttrID.TRAINER_TYPE)
            == TrainerType.SUPPORTER.value)

async def psychic_research(ctx):
    """A Supporter from the discard pile is used as this attack's effect; the
    card stays in the discard pile."""
    supporters = [card for card in ctx.discard_pile() if _is_supporter(card)]
    if not supporters:
        return
    picks = await ctx.choose_cards(supporters, 1, minimum=1,
                                   prompt="Choose a Supporter card to use")
    if not picks:
        return
    inner = await resolve_trainer_effect(ctx.session, ctx.player_id, picks[0])
    if inner is None:
        return
    await ctx.session._flush_effect_runs(inner)
    inner._messages.clear()

card = PokemonCardDef(
    guid="7cdba2d8-c442-52f8-a22a-fa6dc9e65227",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    display_name="Kirlia",
    searchable_by=["Kirlia", "Stage 1", "Kirlia"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="POP7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Psychic Research",
            game_text="Search your discard pile for a Supporter card and use the effect of that card as the effect of this attack. (The Supporter card remains in your discard pile.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=psychic_research,
        ),
        Attack(
            title="Telekinesis",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(40, pool="any", apply_modifiers=False),
        ),
    ],
)