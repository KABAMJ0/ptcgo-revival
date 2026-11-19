from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def mountain_roasting(ctx):
    """On evolve: you may discard the top 3 cards of your opponent's deck."""
    if await ctx.ask_yes_no("Discard the top 3 cards of your opponent's deck?"):
        await ctx.discard_cards(ctx.deck_top(3, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="142ef8b6-6add-5ad6-b14a-4b5842ae7aa2",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2", "Chandelure"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="SWSH11TG",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Mountain Roasting",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may discard the top 3 cards of your opponent's deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=mountain_roasting,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)