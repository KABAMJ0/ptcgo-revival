from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import is_energy_card
from ptcgo.game.card_effects.trainers import extra_prize_on_ko

async def eat_sloppily(ctx):
    """Discard the top 5 of your deck, then attach any Energy among them to
    this Pokemon."""
    top = ctx.deck_top(5)
    if not top:
        return
    await ctx.discard_cards(top)
    for card in top:
        if is_energy_card(card):
            await ctx.attach_energy(card, ctx.attacker)


async def glutton_gx(ctx):
    """100 damage; take 2 more Prizes if that Knocks Out their Active."""
    await extra_prize_on_ko(lambda p: True, prizes=2)(ctx)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="c968be91-9fc6-5a57-805a-740e910a1abd",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GuzzlordGX.Name",
    display_name="Guzzlord-GX",
    searchable_by=["Guzzlord-GX", "Basic", "GX", "Ultra Beast", "GuzzlordGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=116,
    set_code="SM4",
    rarity=Rarities.RareRainbow,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=799,
    abilities=[
        Attack(
            title="Eat Sloppily",
            game_text="Discard the top 5 cards of your deck. If any of those cards are Energy cards, attach them to this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=eat_sloppily,
        ),
        Attack(
            title="Tyrannical Hole",
            cost={PokemonTypes.DARKNESS: 3, PokemonTypes.COLORLESS: 2},
            damage=180,
        ),
        Attack(
            title="Glutton-GX",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from this attack, take 2 more Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 5},
            damage=100,
            effect=glutton_gx,
        ),
    ],
)