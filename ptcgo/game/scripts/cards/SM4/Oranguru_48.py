from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_tool_card


async def fixer_of_the_forest(ctx):
    """Put 3 Pokemon Tool cards from your discard pile into your hand."""
    tools = [card for card in ctx.discard_pile() if is_tool_card(card)]
    if not tools:
        return
    picks = await ctx.choose_cards(
        tools, 3, minimum=min(3, len(tools)),
        prompt="Choose 3 Pokémon Tool cards to put into your hand")
    if picks:
        await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="51828f4d-b3a1-55d9-8f9a-a2908109d60e",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oranguru.Name",
    display_name="Oranguru",
    searchable_by=["Oranguru", "Basic", "Oranguru"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="SM4",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=765,
    abilities=[
        Attack(
            title="Fixer of the Forest",
            game_text="Put 3 Pok\u00e9mon Tool cards from your discard pile into your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=fixer_of_the_forest,
        ),
        Attack(
            title="Zen Headbutt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)