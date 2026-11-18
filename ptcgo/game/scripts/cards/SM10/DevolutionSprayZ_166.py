from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import AttrID, PokemonStage, Rarities
from ptcgo.game.models.board import PokemonEntity


async def _devolution_spray_z(ctx):
    evolved = [pokemon for pokemon in ctx.my_pokemon_in_play()
               if pokemon.get_attribute(AttrID.STAGE)
               not in (None, PokemonStage.BASIC.value)]
    if not evolved:
        return
    target = await ctx.choose_pokemon(
        evolved, "Choose a Pok\u00e9mon to devolve") \
        if len(evolved) > 1 else evolved[0]
    if target is None:
        return
    slot = ctx.board.bench_slot_of(target)
    area = target.parent
    stages = [card for card in target.children if isinstance(card, PokemonEntity)]
    picks = await ctx.choose_cards(
        stages, len(stages), minimum=1,
        prompt="Choose any number of Evolution cards to shuffle into your deck")
    if not picks:
        return
    if not await ctx.devolve_pokemon(target, steps=len(picks), destination="deck"):
        return
    await ctx.shuffle_deck()
    remaining = [card for card in (area.children if area is not None else [])
                 if isinstance(card, PokemonEntity)
                 and ctx.board.bench_slot_of(card) == slot]
    if remaining:
        ctx.session.turn_state.mark_entered_play(remaining[0].entity_id)


card = ItemCardDef(
    guid="cd6aad16-2ac2-5568-a8d3-098477c3d15d",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DevolutionSprayZ.Name",
    display_name="Devolution Spray Z",
    searchable_by=["Devolution Spray Z", "Item"],
    subtypes=["Item"],
    collector_number=166,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=_devolution_spray_z
)
