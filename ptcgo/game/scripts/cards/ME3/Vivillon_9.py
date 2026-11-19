from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def grand_wing(ctx):
    """Opponent shuffles their hand to the bottom of their deck; if they
    did, they draw 4."""
    moved = await ctx.hand_to_bottom_of_deck(ctx.opponent_id)
    if moved > 0:
        await ctx.draw_cards(4, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="bb0be1bd-85ea-5752-a90e-c1defdfc4c79",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name",
    display_name="Vivillon",
    searchable_by=["Vivillon", "Stage 2", "Vivillon"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    family_id=664,
    abilities=[
        Ability(
            title="Grand Wing",
            game_text="Once during your turn, you may use this Ability. Your opponent shuffles their hand and puts it on the bottom of their deck. If they put any cards on the bottom of their deck in this way, they draw 4 cards.",
            activation=Activations.ONCE_PER_TURN,
            effect=grand_wing,
        ),
        Attack(
            title="Blow Through",
            game_text="If a Stadium is in play, this attack does 60 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)