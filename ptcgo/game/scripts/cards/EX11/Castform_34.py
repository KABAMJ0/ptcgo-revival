from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, def_for, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import swap_with_named
from ptcgo.game.scripts.cards import loader as card_loader

_CASTFORM_FORMS = {"sunny castform", "rain castform", "snow-cloud castform"}


def _is_castform_form(card):
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower() \
        in _CASTFORM_FORMS


async def _shuffle_away_outgoing(ctx, incoming):
    await ctx.shuffle_deck()


def _has_holon_energy(ctx):
    for energy in ctx.attached_energies(ctx.attacker):
        card = card_loader.cards_by_guid.get((energy.archetype_id or "").lower())
        if card is not None and "holon" in (getattr(card, "display_name", "") or "").lower():
            return True
    return False


async def _holon_draw(ctx):
    await ctx.draw_cards(1, ctx.player_id)
    if _has_holon_energy(ctx):
        await ctx.draw_cards(2, ctx.player_id)


card = PokemonCardDef(
    guid="a0b5de83-fb13-5903-9791-e51d838cc233",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Castform.Name",
    display_name="Castform",
    searchable_by=["Castform", "Basic", "Castform"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=351,
    abilities=[
        Ability(
            title="Temperamental Weather",
            game_text="Once during your turn (before your attack), you may search your deck for Sunny Castform, Rain Castform, or Snow-cloud Castform and switch it with Castform. (Any cards attached to Castform, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) Shuffle Castform back into your deck. You can't use more than 1 Temperamental Weather Pok\u00e9-Power each turn.",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Temperamental Weather",
            effect=swap_with_named(predicate=_is_castform_form, destination="deck",
                                   then=_shuffle_away_outgoing),
        ),
        Attack(
            title="Holon Draw",
            game_text="Draw a card. If Castform has any Holon Energy cards attached to it, draw 2 more cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_holon_draw,
        ),
    ],
)