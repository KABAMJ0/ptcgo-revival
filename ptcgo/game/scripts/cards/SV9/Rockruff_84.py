from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per, count_bench, has_attack_titled

async def dig_it_up(ctx):
    """Look at the top card of your deck. You may discard that card."""
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    idx = await ctx.present_card_choice(
        card, "Discard this card?", ["Discard", "Keep on top"])
    if idx == 0:
        await ctx.discard_cards([card])


async def dig_it_up(ctx):
    """Look at the top card of your deck. You may discard that card."""
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    idx = await ctx.present_card_choice(
        card, "Discard this card?", ["Discard", "Keep on top"])
    if idx == 0:
        await ctx.discard_cards([card])


card = PokemonCardDef(
    guid="89ef2adf-667b-5247-b226-39f994bafbc9",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    display_name="Rockruff",
    searchable_by=["Rockruff", "Basic", "Rockruff"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=744,
    abilities=[
        Attack(
            title="Dig It Up",
            game_text="Look at the top card of your deck. You may discard that card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=dig_it_up,
        ),
        Attack(
            title="Stampede",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)