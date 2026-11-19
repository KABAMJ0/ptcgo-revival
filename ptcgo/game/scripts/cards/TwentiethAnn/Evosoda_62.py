from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import AttrID, Rarities
from ptcgo.game.content.definitions import evolves_from


def evosoda_playable(board, player_id):
    state = getattr(board, "turn_state", None)
    return state is None or state.turn_number > 2


async def evosoda(ctx):
    state = getattr(ctx.board, "turn_state", None)
    turn = getattr(state, "turn_number", 0)
    entered = getattr(state, "entered_play_turn", None) or {}
    pool = [p for p in ctx.my_pokemon_in_play()
            if entered.get(p.entity_id, 0) != turn]
    if not pool:
        return
    target = (await ctx.choose_pokemon(pool, "Choose a Pok\u00e9mon to evolve")
              if len(pool) > 1 else pool[0])
    if target is None:
        return
    logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)

    def eligible(card):
        return bool(logic_name) and evolves_from(
            getattr(card, "archetype_id", None) or "", logic_name)

    picks = await ctx.search_deck(
        eligible, count=1, minimum=0,
        prompt="Choose an Evolution card for this Pok\u00e9mon")
    if picks:
        await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="ca2bd6d8-84a7-590d-94e7-06477560f1f0",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Evosoda.Name",
    display_name="Evosoda",
    searchable_by=["Evosoda", "Item"],
    subtypes=["Item"],
    collector_number=62,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=evosoda,
    condition=evosoda_playable,
)
