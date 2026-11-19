from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.pokemon import is_water_energy


async def _aqua_stream(ctx):
    cards = [card for card in ctx.discard_pile() if is_water_energy(card)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, len(cards), minimum=0,
        prompt="Choose any number of Water Energy cards to put on top of your deck")
    if not picks:
        return
    await ctx.reveal_cards(picks, to_player=ctx.opponent_id)
    await ctx.deal_damage(10 * len(picks))
    for card in picks:
        await ctx.put_on_top_of_deck(card)
    await ctx.shuffle_deck()


async def _dragon_pump(ctx):
    hand = list(ctx.hand())
    picks = await ctx.choose_cards(
        hand, 2, minimum=0,
        prompt="Discard 2 cards to do 20 more damage") if hand else []
    if picks:
        await ctx.discard_cards(picks)
    bonus = len(picks) == 2
    await ctx.deal_damage(40 + (20 if bonus else 0))
    if bonus:
        await snipe_attack(20, pool="bench", count=1)(ctx)


card = PokemonCardDef(
    guid="0567474d-c7bf-55fa-8d4a-ebcd474e98e0",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Attack(
            title="Aqua Stream",
            game_text="Search your discard pile for as many Water Energy cards as you like, show them to your opponent, and this attack does 10 damage for each Water Energy card you chose. Put those cards on top of your deck. Shuffle your deck afterward.",
            cost={},
            damage=10,
            damage_operator="x",
            effect=_aqua_stream,
        ),
        Attack(
            title="Dragon Pump",
            game_text="You may discard 2 cards from your hand. If you do, this attack does 40 damage plus 20 more damage and does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            damage=40,
            damage_operator="+",
            effect=_dragon_pump,
        ),
    ],
)