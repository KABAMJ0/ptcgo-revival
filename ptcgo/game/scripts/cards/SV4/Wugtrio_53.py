from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_tool_card


async def _suddenly_select(ctx):
    """On evolve: optionally search up to 3 Pokemon Tool cards into hand."""
    if not await ctx.ask_yes_no(
            "Search your deck for up to 3 Pokémon Tool cards?"):
        return
    picks = await ctx.search_deck(
        is_tool_card, count=3, minimum=0,
        prompt="Choose up to 3 Pokémon Tool cards.",
    )
    await ctx.put_in_hand(picks)
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="bc8383d1-fce0-5448-9221-5d078bbb50ea",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wugtrio.Name",
    display_name="Wugtrio",
    searchable_by=["Wugtrio", "Stage 1", "Wugtrio"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name",
    family_id=960,
    abilities=[
        Ability(
            title="Suddenly Select",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may search your deck for up to 3 Pok\u00e9mon Tool cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=_suddenly_select,
        ),
        Attack(
            title="Triple Whip",
            game_text="Flip 3 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.WATER: 2},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)