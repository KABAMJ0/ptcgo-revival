from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _psychic_strategy(ctx):
    mine = ctx.hand_size(ctx.player_id)
    theirs = ctx.hand_size(ctx.opponent_id)
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    await ctx.draw_cards(theirs)
    await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
    await ctx.draw_cards(mine, ctx.opponent_id)


async def _super_eggsplosion(ctx):
    pool = [energy for pokemon in ctx.my_pokemon_in_play()
            for energy in ctx.attached_energies(pokemon)]
    picks = await ctx.choose_cards(
        pool, len(pool), minimum=0,
        prompt="Choose any number of Energy cards to discard") if pool else []
    if picks:
        await ctx.discard_cards(picks)
    heads = 0
    for _ in picks:
        results = await ctx.flip_coins(1, "Super Eggsplosion")
        if results and results[0]:
            heads += 1
    if heads:
        await ctx.deal_damage(50 * heads)


card = PokemonCardDef(
    guid="2328993a-c00a-5bcd-81d5-d6b85b456f33",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name",
    display_name="Exeggutor",
    searchable_by=["Exeggutor", "Stage 1", "Exeggutor"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Psychic Strategy",
            game_text="Each player counts the number of cards in his or her opponent's hand. Each player shuffles his or her hand into his or her deck. Then, each player draws a number of cards up to the number of cards his or her opponent had. (You draw your cards first.)",
            cost={},
            effect=_psychic_strategy,
        ),
        Attack(
            title="Super Eggsplosion",
            game_text="Discard as many Energy cards as you like attached to your Pok\u00e9mon. For each Energy card you discarded, flip a coin. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="x",
            effect=_super_eggsplosion,
        ),
    ],
)