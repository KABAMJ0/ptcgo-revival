from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack
from ptcgo.game.data_utils import Triggers, def_for


async def _time_walk(ctx):
    prizes = ctx.face_down_prize_cards(ctx.player_id)
    if not prizes:
        return
    await ctx.reveal_cards(prizes)
    picks = await ctx.choose_cards(
        prizes, 1, minimum=0,
        prompt="Choose a Pok\u00e9mon from your Prizes to put into your hand")
    if not picks:
        return
    if not isinstance(def_for(picks[0].archetype_id), PokemonCardDef):
        return
    await ctx.put_in_hand(picks, reveal=True)
    hand = [card for card in ctx.hand() if card is not picks[0]]
    if not hand:
        return
    swap = await ctx.choose_cards(
        hand, 1, minimum=1,
        prompt="Choose a card from your hand to put as a Prize card face down")
    if swap:
        await ctx.put_in_prizes(swap)


async def _time_walk(ctx):
    prizes = ctx.face_down_prize_cards(ctx.player_id)
    if not prizes:
        return
    await ctx.reveal_cards(prizes)
    picks = await ctx.choose_cards(
        prizes, 1, minimum=0,
        prompt="Choose a Pok\u00e9mon from your Prizes to put into your hand")
    if not picks:
        return
    if not isinstance(def_for(picks[0].archetype_id), PokemonCardDef):
        return
    await ctx.put_in_hand(picks, reveal=True)
    hand = [card for card in ctx.hand() if card is not picks[0]]
    if not hand:
        return
    swap = await ctx.choose_cards(
        hand, 1, minimum=1,
        prompt="Choose a card from your hand to put as a Prize card face down")
    if swap:
        await ctx.put_in_prizes(swap)


card = PokemonCardDef(
    guid="d8e35115-b718-5a85-b387-e8b9348694b8",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azelf.Name",
    display_name="Azelf",
    searchable_by=["Azelf", "Basic", "Azelf"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=482,
    abilities=[
        Ability(
            title="Time Walk",
            trigger=Triggers.ON_PLAY,
            game_text="Once during your turn, when you put Azelf from your hand onto your Bench, you may look at all of your face-down Prize cards. If you do, you may choose 1 Pok\u00e9mon you find there, show it to your opponent, and put it into your hand. Then, choose 1 card in your hand and put it as a Prize card face down.",
            effect=_time_walk,
        ),
        Attack(
            title="Lock Up",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=no_retreat_attack(),
        ),
    ],
)