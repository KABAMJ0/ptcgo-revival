import random

from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.session.effects import is_special_energy


def _prize_shift_condition(board, player_id, pokemon) -> bool:
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    area = board.find_player_area(player_id, "prizePile")
    return any(not getattr(card, "face_up", False)
               for card in (area.children if area else []))


async def _prize_shift(ctx):
    """A hand card goes into the Prizes face up; a face-down Prize comes back
    to hand unseen."""
    hand = ctx.hand()
    if not hand:
        return
    picked = await ctx.choose_cards(
        hand, 1, minimum=1,
        prompt="Choose a card to put as a face-up Prize card")
    if not picked or not await ctx.put_in_prizes(picked, face_up=True):
        return
    face_down = ctx.face_down_prize_cards()
    if face_down:
        await ctx.put_in_hand([random.choice(face_down)], reveal=False)


def _provides(energies, type_value) -> bool:
    return any(energy_provides_type(energy, type_value) for energy in energies)


async def _psychic_option(ctx):
    energies = ctx.attached_energies(ctx.attacker)
    bonus = 20 if _provides(energies, PokemonTypes.WATER.value) else 0
    await ctx.deal_damage(20 + bonus)
    if _provides(energies, PokemonTypes.PSYCHIC.value):
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.discard_energy_from(
                defender, 1, predicate=is_special_energy,
                prompt="Choose a Special Energy to discard")


card = PokemonCardDef(
    guid="f342d939-91d1-514d-a6a5-f7b7117fe18a",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name",
    display_name="Slowking",
    searchable_by=["Slowking", "Stage 1", "Slowking"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Prize Shift",
            game_text="Once during your turn (before your attack), you may choose a card from your hand and put it as a Prize card face up. If you do, choose 1 of your face-down Prize cards without looking and put it into your hand. This power can't be used if Slowking is affected by a Special Condition or if all of your Prize cards are face up.",
            activation=Activations.ONCE_PER_TURN,
            condition=_prize_shift_condition,
            effect=_prize_shift,
        ),
        Attack(
            title="Psychic Option",
            game_text="If Slowking has a Water Energy card attached to it, this attack does 20 damage plus 20 more damage. If Slowking has a Psychic Energy card attached to it, discard a Special Energy card attached to the Defending Pok\u00e9mon, if any.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=_psychic_option,
        ),
    ],
)