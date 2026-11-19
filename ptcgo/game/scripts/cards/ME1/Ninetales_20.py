from ptcgo.game.data_utils import (
    PokemonCardDef, Attack, TRAINER_EFFECTS_BY_GUID, unimplemented,
)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_supporter_card


def _runnable_supporter(card) -> bool:
    if not is_supporter_card(card):
        return False
    effect = TRAINER_EFFECTS_BY_GUID.get((card.archetype_id or "").lower())
    return effect is not None and effect is not unimplemented


async def supernatural_shapeshifter(ctx):
    """Discard the top card of your deck; if it is a Supporter, use its
    effect as this attack's effect."""
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    await ctx.discard_cards([card])
    if not _runnable_supporter(card):
        return
    await TRAINER_EFFECTS_BY_GUID[(card.archetype_id or "").lower()](ctx)


card = PokemonCardDef(
    guid="a6b3963b-1dae-5ee5-b522-ffaa14a5c2c0",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Supernatural Shapeshifter",
            game_text="Discard the top card of your deck, and if that card is a Supporter card, use the effect of that card as the effect of this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=supernatural_shapeshifter,
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)