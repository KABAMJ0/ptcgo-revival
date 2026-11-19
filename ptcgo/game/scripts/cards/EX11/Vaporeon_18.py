from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.support_common import (
    return_attached_energy, search_attach_energy)


def _is_holon_energy(card):
    from ptcgo.game.scripts.cards import loader as card_loader
    definition = card_loader.cards_by_guid.get((getattr(card, "archetype_id", "") or "").lower())
    return definition is not None and \
        (getattr(definition, "display_name", "") or "").lower().startswith("holon energy")


async def _return_defender_energy(ctx, returned):
    """The "if you do" half: one Energy on the Defending Pokemon goes back to
    the opponent's hand."""
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    energies = list(ctx.attached_energies(defender))
    if not energies:
        return
    picks = energies if len(energies) == 1 else await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose an Energy card to return to your opponent's hand")
    hand = ctx.board.find_player_area(ctx.opponent_id, "hand")
    for card in picks:
        ctx.board.move_card(card.entity_id, hand.entity_id)


card = PokemonCardDef(
    guid="8aa2c804-b99d-5b65-bcc0-18320cc2f232",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon δ",
    searchable_by=["Vaporeon \u03b4", "Stage 1", "Vaporeon"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER, PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Delta Search",
            game_text="Search your deck for a Holon Energy card and attach it to Vaporeon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=search_attach_energy(_is_holon_energy, count=1, to_self=True),
        ),
        Attack(
            title="Return Wave",
            game_text="You may return an Energy card attached to Vaporeon to your hand. If you do, choose an Energy card attached to the Defending Pok\u00e9mon and return it to your opponent's hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=composed(
                lambda ctx: ctx.deal_damage(),
                return_attached_energy(count=1, target="self",
                                       then=_return_defender_energy)),
        ),
    ],
)