from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import discard_random_from_hand
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _flip_discard(ctx):
    await ctx.deal_damage()
    if any(await ctx.flip_coins(1, "Flip a coin")):
        await discard_random_from_hand(ctx, ctx.opponent_id)


card = PokemonCardDef(
    guid="1af23bdc-e537-5e89-8de5-fa98edc8f3e3",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    display_name="Wimpod",
    searchable_by=["Wimpod", "Basic", "Wimpod"],
    subtypes=["Basic"],
    collector_number=191,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=767,
    abilities=[
        Attack(
            title="Sneaky Snacking",
            game_text="Flip a coin. If heads, discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_flip_discard,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)