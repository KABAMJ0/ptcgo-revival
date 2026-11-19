from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import (
    discard_tool_at_end_of_turn, is_pokemon_EX, is_pokemon_ex, is_tool_card,
)
from ptcgo.game.card_effects.passives_common import apply_protection
from ptcgo.game.data_utils import def_for
from ptcgo.game.session.effects import is_evolution_pokemon


def _has_owner_in_name(card):
    name = (getattr(def_for(card.archetype_id), "display_name", "") or "")
    return "'s " in name.replace("\u2019", "'")


def _legal_holder(card):
    return is_evolution_pokemon(card) \
        and not (is_pokemon_ex(card) or is_pokemon_EX(card)) \
        and not _has_owner_in_name(card)


async def _ice_generator(ctx):
    doomed = [child for pokemon in ctx.opponent_pokemon_in_play()
              for child in pokemon.children if is_tool_card(child)]
    stadium = ctx.stadium_in_play()
    if stadium is not None and stadium.owning_player_id == ctx.opponent_id:
        doomed.append(stadium)
    if not doomed:
        return
    await ctx.discard_cards(doomed)
    await apply_protection(ctx, target=ctx.attacker, prevent=True,
                           effects_too=True)


card = PokemonToolCardDef(
    guid="c13abb70-a9c8-5f6f-a79d-f6d4538ee2dd",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientTechnicalMachineIce.Name",
    display_name="Ancient Technical Machine [Ice]",
    searchable_by=["Ancient Technical Machine [Ice]", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=84,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    attach_to=_legal_holder,
    granted_abilities=[
        Attack(
            title="Ice Generator",
            game_text="Discard all of your opponent's Trainer cards in play. "
                      "If you do, prevent all effects, including damage, done "
                      "to the Pok\u00e9mon using this attack during your "
                      "opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_ice_generator,
        ),
        Ability(
            title="Ancient Technical Machine [Ice]",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
