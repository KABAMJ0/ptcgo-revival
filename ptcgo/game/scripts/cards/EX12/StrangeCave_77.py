from ptcgo.game.data_utils import StadiumCardDef, Ability, Activations
from ptcgo.game.attributes import PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import card_named_any

_FOSSIL_NAMES = ("omanyte", "kabuto", "aerodactyl", "lileep", "anorith")
_IS_FOSSIL = card_named_any(_FOSSIL_NAMES)


async def _strange_cave(ctx):
    pool = [card for card in ctx.hand() if _IS_FOSSIL(card)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1, minimum=0,
        prompt="Choose a Pok\u00e9mon to put onto your Bench")
    if not picks:
        return
    card = picks[0]
    if await ctx.bench_pokemon(card):
        benched = ctx.board.get_entity(card.entity_id)
        if benched is not None:
            ctx.set_pokemon_stage(benched, PokemonStage.BASIC)


def _strange_cave_ready(board, player_id, card=None):
    hand = board.find_player_area(player_id, "hand")
    return any(_IS_FOSSIL(c) for c in (hand.children if hand else []))


card = StadiumCardDef(
    guid="63c43f33-e962-5a4d-b257-1681e7abfeef",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrangeCave.Name",
    display_name="Strange Cave",
    searchable_by=["Strange Cave", "Stadium"],
    subtypes=["Stadium"],
    collector_number=77,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Strange Cave",
        game_text="Once during each player's turn, that player may put an Omanyte, "
                  "Kabuto, Aerodactyl, Aerodactyl ex, Lileep, or Anorith onto his "
                  "or her Bench from his or her hand. Treat the new Benched "
                  "Pok\u00e9mon as Basic Pok\u00e9mon.",
        activation=Activations.ONCE_PER_TURN,
        condition=_strange_cave_ready,
        effect=_strange_cave,
    ),
)
