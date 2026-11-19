from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_tool_card


async def intentional_grounding(ctx):
    """Printed 90 only when a Pokemon Tool card is discarded from your hand;
    declining (or holding no Tool) leaves the attack with no damage."""
    tools = [card for card in ctx.hand() if is_tool_card(card)]
    if not tools:
        return
    picked = await ctx.choose_cards(
        tools, 1, minimum=0,
        prompt="Discard a Pokémon Tool card from your hand")
    if not picked:
        return
    await ctx.discard_cards(picked)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="b381e864-d1b3-560c-bfc0-7f1eca539c60",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Passimian.Name",
    display_name="Passimian",
    searchable_by=["Passimian", "Basic", "Passimian"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=766,
    abilities=[
        Attack(
            title="Punch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Intentional Grounding",
            game_text="Discard a Pok\u00e9mon Tool card from your hand. If you don't, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=90,
            effect=intentional_grounding,
        ),
    ],
)