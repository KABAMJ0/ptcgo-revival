from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import AttrID, Rarities


async def _breeder_fields(ctx):
    def later_stage(card, logic_name):
        return card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == logic_name

    def can_evolve(pokemon):
        logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        return bool(logic_name) and any(
            later_stage(card, logic_name) for card in ctx.deck())

    pool = [pokemon for pokemon in ctx.my_pokemon_in_play() if can_evolve(pokemon)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 2, minimum=1,
        prompt="Choose 1 or 2 Pok\u00e9mon that can evolve")
    found = []
    for pokemon in picks:
        if not (await ctx.flip_coins(1, title="Pok\u00e9mon Breeder Fields"))[0]:
            continue
        logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        found.extend(await ctx.search_deck(
            lambda card, name=logic_name: later_stage(card, name),
            count=1, minimum=0,
            prompt="Choose a card that evolves from this Pok\u00e9mon"))
    if found:
        await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="8090d85b-69f9-5447-b33f-50706305fadc",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonBreederFields.Name",
    display_name="Pok\u00e9mon Breeder Fields",
    searchable_by=["Pok\u00e9mon Breeder Fields"],
    subtypes=[],
    collector_number=62,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    effect=_breeder_fields
)
