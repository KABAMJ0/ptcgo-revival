from ptcgo.game.data_utils import StadiumCardDef, Ability, Activations
from ptcgo.game.attributes import PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import pokemon_of_subtype

_IS_RESTORED = pokemon_of_subtype("Restored")


async def _twist_mountain(ctx):
    heads = (await ctx.flip_coins(1, title="Twist Mountain"))[0]
    if not heads:
        return
    pool = [card for card in ctx.hand() if _IS_RESTORED(card)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1, minimum=0,
        prompt="Choose a Restored Pok\u00e9mon to put onto your Bench")
    if not picks:
        return
    card = picks[0]
    if await ctx.bench_pokemon(card):
        benched = ctx.board.get_entity(card.entity_id)
        if benched is not None:
            ctx.set_pokemon_stage(benched, PokemonStage.BASIC)


def _twist_mountain_ready(board, player_id, card=None):
    hand = board.find_player_area(player_id, "hand")
    return any(_IS_RESTORED(c) for c in (hand.children if hand else []))


card = StadiumCardDef(
    guid="2806afe9-470b-5e2a-97fc-70e5f49720a3",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TwistMountain.Name",
    display_name="Twist Mountain",
    searchable_by=["Twist Mountain", "Stadium"],
    subtypes=["Stadium"],
    collector_number=101,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Twist Mountain",
        game_text="Once during each player's turn, that player may flip a coin. "
                  "If heads, that player may play a Restored Pok\u00e9mon from "
                  "their hand onto their Bench.",
        activation=Activations.ONCE_PER_TURN,
        condition=_twist_mountain_ready,
        effect=_twist_mountain,
    ),
)
