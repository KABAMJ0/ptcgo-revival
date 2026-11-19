from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID, TrainerType
from ptcgo.game.data_utils import Triggers


def _is_pokemon_tool(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value


async def _gift(ctx):
    for player_id in (ctx.opponent_id, ctx.player_id):
        picks = await ctx.search_deck(
            _is_pokemon_tool, count=1, minimum=0, player_id=player_id,
            prompt="Search your deck for a Pok\u00e9mon Tool card")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
            await ctx.shuffle_deck(player_id)


async def _sweet_kiss(ctx):
    await ctx.deal_damage()
    if await ctx.ask_yes_no("Draw a card?", player_id=ctx.opponent_id):
        await ctx.draw_cards(1, ctx.opponent_id)


card = PokemonCardDef(
    guid="0aef6db5-c560-5698-9550-43244bc51a68",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightTogetic.Name",
    display_name="Light Togetic",
    searchable_by=["Light Togetic", "Stage 1", "LightTogetic"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    family_id=175,
    abilities=[
        Ability(
            title="Gift",
            trigger=Triggers.ON_PLAY,
            game_text="When you play Light Togetic from your hand, your opponent may search his or her deck for a Pok\u00e9mon Tool card, show that card to you, and put it into his or her hand. Either way, you may do the same, and then each player who searched shuffles his or her deck.",
            effect=_gift,
        ),
        Attack(
            title="Sweet Kiss",
            game_text="Your opponent may draw a card.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_sweet_kiss,
        ),
    ],
)