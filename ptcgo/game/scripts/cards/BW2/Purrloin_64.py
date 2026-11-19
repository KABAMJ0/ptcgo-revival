from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import discard_random_from_hand
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _flip_discard(ctx):
    await ctx.deal_damage()
    if any(await ctx.flip_coins(1, "Flip a coin")):
        await discard_random_from_hand(ctx, ctx.opponent_id)


card = PokemonCardDef(
    guid="d3fb6fcc-33f9-5e7d-9357-20ef3e96d4a7",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    display_name="Purrloin",
    searchable_by=["Purrloin", "Basic", "Purrloin"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="BW2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=509,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Flip a coin. If heads, discard a random card from your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_flip_discard,
        ),
    ],
)