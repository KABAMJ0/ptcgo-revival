from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def twister_spewing(ctx):
    """80 damage; if you played Tarragon from your hand this turn, also
    discard the top 3 cards of your opponent's deck."""
    await ctx.deal_damage()
    if ctx.played_trainer_this_turn("Tarragon") > 0:
        milled = ctx.deck_top(3, player_id=ctx.opponent_id)
        if milled:
            await ctx.discard_cards(milled)


card = PokemonCardDef(
    guid="0f55668d-a337-547a-9f15-778d37a03c64",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippowdon.Name",
    display_name="Hippowdon",
    searchable_by=["Hippowdon", "Stage 1", "Hippowdon"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    family_id=449,
    abilities=[
        Attack(
            title="Twister Spewing",
            game_text="If you played Tarragon from your hand during this turn, discard the top 3 cards of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=twister_spewing,
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
        ),
    ],
)