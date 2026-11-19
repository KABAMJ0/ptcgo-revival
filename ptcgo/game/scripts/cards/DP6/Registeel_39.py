from ptcgo.game.card_effects.passives_common import (
    discard_from_hand_then, effective_max_hp, unafflicted,
)
from ptcgo.game.card_effects.trainers import is_energy_card
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


def _regi_heal_condition(board, player_id, pokemon) -> bool:
    """Regi Heal needs a clean, damaged Registeel."""
    if not unafflicted(board, player_id, pokemon):
        return False
    return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


async def _regi_heal(ctx):
    await ctx.heal(30, ctx.source)


async def _rotating_claws(ctx):
    await ctx.deal_damage()
    if ctx.attacker is None or not ctx.attached_energies(ctx.attacker):
        return
    if not await ctx.ask_yes_no("Discard an Energy card attached to Registeel?"):
        return
    discarded = await ctx.discard_energy_from(ctx.attacker, 1)
    if not discarded:
        return
    skipped = {card.entity_id for card in discarded}
    candidates = [card for card in ctx.discard_pile()
                  if is_energy_card(card) and card.entity_id not in skipped]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="Choose an Energy card to attach to Registeel")
    for card in picks:
        await ctx.attach_energy(card, ctx.attacker)

card = PokemonCardDef(
    guid="f3291f66-4398-5e52-910e-b122da959e12",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Registeel.Name",
    display_name="Registeel",
    searchable_by=["Registeel", "Basic", "Registeel"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=379,
    abilities=[
        Ability(
            title="Regi Heal",
            game_text="Once during your turn (before your attack), you may discard 2 cards from your hand. Then, remove 3 damage counters from Registeel. This power can't be used if Registeel is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_regi_heal_condition,
            effect=discard_from_hand_then(None, 2, then=_regi_heal),
        ),
        Attack(
            title="Rotating Claws",
            game_text="You may discard an Energy card attached to Registeel. If you do, search your discard pile for an Energy card (excluding the one you discarded) and attach it to Registeel.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=_rotating_claws,
        ),
    ],
)