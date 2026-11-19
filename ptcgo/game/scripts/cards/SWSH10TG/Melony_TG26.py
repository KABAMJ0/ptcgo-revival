from ptcgo.game.data_utils import SupporterCardDef, is_pokemon_v
from ptcgo.game.attributes import Rarities, PokemonTypes
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import (
    attach_from_discard, requires_discard, requires_in_play,
)
from ptcgo.game.card_effects.pokemon import is_water_energy


def _is_v_pokemon(pokemon):
    return is_pokemon_v(pokemon.archetype_id)


def _melony_condition(board, player_id):
    return (
        requires_discard(is_water_energy)(board, player_id)
        and requires_in_play(_is_v_pokemon, side="mine")(board, player_id)
    )


async def _melony_draw(ctx, picks):
    await ctx.draw_cards(3)


melony = attach_from_discard(
    predicate=is_water_energy, target=_is_v_pokemon, then=_melony_draw,
    prompt="Choose a Water Energy card to attach.",
)

card = SupporterCardDef(
    guid="a98bd149-c369-5404-9e43-3c6bf3a1ff31",
    key="SWSH10TG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Melony.Name",
    display_name="Melony",
    searchable_by=["Melony", "Supporter"],
    subtypes=["Supporter"],
    collector_number=26,
    set_code="SWSH10TG",
    rarity=Rarities.RareUltra,
    effect=melony,
    condition=_melony_condition,
)
