from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import full_stack


async def strong_breeze(ctx):
    """The Defending Pokemon and everything attached go into its owner's deck;
    the opponent then promotes a new Active."""
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.shuffle_into_deck(full_stack(defender), ctx.opponent_id)

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.opponent_id):
            screen_name = ctx.session.players[ctx.opponent_id].screen_name
            await ctx.session.end_game(
                ctx.player_id, f"{screen_name} has no Pok\u00e9mon left")
    ctx.deferred_actions.append(_promote)

card = PokemonCardDef(
    guid="8615af42-d009-50c3-9a47-11ad919be95b",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name",
    display_name="Staraptor",
    searchable_by=["Staraptor", "Stage 2", "Staraptor"],
    subtypes=["Stage 2"],
    collector_number=97,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
        Attack(
            title="Strong Breeze",
            game_text="Your opponent shuffles the Defending Pok\u00e9mon and all cards attached to it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 4},
            effect=strong_breeze,
        ),
    ],
)