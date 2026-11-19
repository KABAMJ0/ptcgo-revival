from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, subtypes_for
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_basic_pokemon


def _baby_or_basic(card) -> bool:
    return ("Baby" in subtypes_for(getattr(card, "archetype_id", "") or "")
            or is_basic_pokemon(card))


async def _look_at_hands_then_bench(ctx):
    """Their Baby/Basic Pokemon come out of their hand onto their Bench (you
    pick), then yours do the same under their choice."""
    their_hand = await ctx.reveal_hand(of_player=ctx.opponent_id,
                                       to_player=ctx.player_id)
    theirs = [card for card in their_hand if _baby_or_basic(card)]
    if theirs:
        picks = await ctx.choose_cards(
            theirs, len(theirs), minimum=0,
            prompt="Choose any number of Baby or Basic Pok\u00e9mon to put onto your opponent's Bench")
        for card in picks:
            await ctx.bench_pokemon(card)

    mine = [card for card in ctx.hand() if _baby_or_basic(card)]
    if not mine:
        return
    mine_picks = await ctx.choose_cards(
        mine, len(mine), minimum=0, player_id=ctx.opponent_id,
        prompt="Choose any number of your Baby or Basic Pok\u00e9mon to put onto your Bench")
    for card in mine_picks:
        await ctx.bench_pokemon(card)


async def _battle_frenzy(ctx):
    """One flip per Pokemon in play, both sides; heads puts 20 on that Pokemon."""
    everyone = list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play())
    results = await ctx.flip_coins(len(everyone), "Battle Frenzy")
    for pokemon, result in zip(everyone, results):
        if result:
            await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)

card = PokemonCardDef(
    guid="8ddb0501-7a4f-5f83-aef1-282da4c14eab",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkUrsaring.Name",
    display_name="Dark Ursaring",
    searchable_by=["Dark Ursaring", "Stage 1", "DarkUrsaring"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    family_id=217,
    abilities=[
        Attack(
            title="Provoke",
            game_text="Look at your opponent's hand. If he or she has any Baby Pok\u00e9mon and/or Basic Pok\u00e9mon there, you may put any number of them onto your opponent's Bench (as long as there's room). Then, your opponent looks at your hand. If you have any Baby Pok\u00e9mon and/or Basic Pok\u00e9mon there, your opponent may put any number of them onto your Bench (as long as there's room).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_look_at_hands_then_bench,
        ),
        Attack(
            title="Battle Frenzy",
            game_text="For each Pok\u00e9mon in play (yours and your opponent's), flip a coin. For each heads, this attack does 20 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance for this attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_battle_frenzy,
        ),
    ],
)