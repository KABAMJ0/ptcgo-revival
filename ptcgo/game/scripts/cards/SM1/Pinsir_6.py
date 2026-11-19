from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.session.effects import full_stack


async def _roof_fling(ctx):
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.put_in_hand(full_stack(target), reveal=False)

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.opponent_id):
            screen_name = ctx.session.players[ctx.opponent_id].screen_name
            await ctx.session.end_game(
                ctx.player_id, f"{screen_name} has no Pok\u00e9mon left")
    ctx.deferred_actions.append(_promote)


roof_fling = flip_gate(_roof_fling)


card = PokemonCardDef(
    guid="940b8253-3e10-53bc-820d-1056af4ce51e",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir",
    searchable_by=["Pinsir", "Basic", "Pinsir"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Roof Fling",
            game_text="Flip a coin. If heads, put your opponent's Active Pok\u00e9mon and all cards attached to it into your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=roof_fling,
        ),
        Attack(
            title="Guillotine",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
        ),
    ],
)