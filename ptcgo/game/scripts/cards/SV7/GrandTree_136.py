from ptcgo.game.data_utils import StadiumCardDef, def_for
from ptcgo.game.attributes import AttrID, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_stage_one, is_stage_two, stadium_ability
from ptcgo.game.content.definitions import evolves_from


def _stage_one_choices(ctx):
    """(Basic in play, Stage 1 archetype in the deck) pairs this player may
    evolve, honouring "can't evolve a Basic during their first turn or a Basic
    put into play this turn"."""
    choices = []
    deck = list(ctx.deck())
    for basic in ctx.my_pokemon_in_play():
        if basic.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value:
            continue
        if not ctx.board.turn_state.may_evolve_target(basic.entity_id):
            continue
        logic_name = basic.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        if not logic_name:
            continue
        seen = set()
        for card in deck:
            if card.archetype_id in seen:
                continue
            if is_stage_one(card) and evolves_from(card.archetype_id, logic_name):
                seen.add(card.archetype_id)
                choices.append((basic, card.archetype_id))
    return choices


def _stage_two_in_deck(ctx, stage_one):
    logic_name = stage_one.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not logic_name:
        return None
    for card in ctx.deck():
        if is_stage_two(card) and evolves_from(card.archetype_id, logic_name):
            return card.archetype_id
    return None


def _wearing(pokemon, card) -> bool:
    """Whether `card` now sits anywhere in `pokemon`'s stack."""
    stack = list(getattr(pokemon, "children", []) or [])
    while stack:
        entity = stack.pop()
        if entity is card or entity.entity_id == card.entity_id:
            return True
        stack.extend(getattr(entity, "children", []) or [])
    return False


async def _grand_tree(ctx):
    """Once during each player's turn, that player may evolve a Basic in play
    into a Stage 1 from the deck, then (if it evolved that way) into a Stage 2
    from the deck."""
    choices = _stage_one_choices(ctx)
    if not choices:
        return
    picked = await ctx.choose(
        "Choose the Pokémon to evolve",
        [f"{def_for(archetype_id).display_name} on "
         f"{def_for(basic.archetype_id).display_name}"
         for basic, archetype_id in choices],
    )
    if picked is None or not 0 <= picked < len(choices):
        return
    basic, stage_one_id = choices[picked]
    stage_one = await ctx.search_deck(
        lambda card: card.archetype_id == stage_one_id,
        count=1, minimum=1,
        prompt="Choose a Stage 1 Pokémon to evolve it into",
    )
    if not await ctx.evolve_pokemon(basic, stage_one[0] if stage_one else None):
        return
    evolved = next((p for p in ctx.my_pokemon_in_play() if _wearing(p, basic)), basic)
    stage_two_id = _stage_two_in_deck(ctx, stage_one[0])
    if stage_two_id is not None:
        stage_two = await ctx.search_deck(
            lambda card: card.archetype_id == stage_two_id,
            count=1, minimum=0,
            prompt="Choose a Stage 2 Pokémon to evolve it into",
        )
        if stage_two:
            await ctx.evolve_pokemon(evolved, stage_two[0])
    await ctx.shuffle_deck()


card = StadiumCardDef(
    guid="f518ed37-8af1-56ba-920f-cecc5462b4b0",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GrandTree.Name",
    display_name="Grand Tree",
    searchable_by=["Grand Tree", "Stadium", "ACE SPEC"],
    subtypes=["Stadium", "ACE SPEC"],
    collector_number=136,
    set_code="SV7",
    rarity=Rarities.Rare,
    ability=stadium_ability("Grand Tree", _grand_tree),
)
