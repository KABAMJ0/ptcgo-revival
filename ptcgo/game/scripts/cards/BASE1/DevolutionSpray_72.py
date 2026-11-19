from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities, AttrID
from ptcgo.game.card_effects.trainers import is_evolution_pokemon
from ptcgo.game.models.board import PokemonEntity


def _evolution_cards(pokemon):
    """The evolution cards tucked under `pokemon`, highest stage first."""
    stages = [card for card in pokemon.children
              if isinstance(card, PokemonEntity)
              and card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)]
    return list(reversed(stages))


async def _devolution_spray(ctx):
    """Choose an evolved Pokemon and a Stage of Evolution: every Evolution
    card of that stage or higher is discarded and the Pokemon loses its
    Special Conditions, exactly as if it had just evolved."""
    pool = [p for p in ctx.my_pokemon_in_play() if is_evolution_pokemon(p)]
    if not pool:
        return
    target = await ctx.choose_pokemon(
        pool, "Choose a Pokémon to devolve") if len(pool) > 1 else pool[0]
    if target is None:
        return
    stages = _evolution_cards(target)
    steps = 1
    if len(stages) > 1:
        steps = 1 + await ctx.choose(
            "Choose the Stage of Evolution to discard from",
            ["Highest Evolution card only", "Every Evolution card"])
    await ctx.cure_all_conditions(target)
    await ctx.devolve_pokemon(target, steps=steps, destination="discard")


card = ItemCardDef(
    guid="52c43ad2-d597-56ab-8dfc-b616de0256c9",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DevolutionSpray.Name",
    display_name="Devolution Spray",
    searchable_by=["Devolution Spray"],
    subtypes=[],
    collector_number=72,
    set_code="BASE1",
    rarity=Rarities.Rare,
    effect=_devolution_spray,
)
