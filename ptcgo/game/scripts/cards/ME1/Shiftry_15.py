from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack, flip_gate
from ptcgo.game.session.effects import full_stack


async def _shuffle_a_defender_away(ctx):
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    chosen = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon")
    if chosen is None:
        return
    was_active = chosen is ctx.opponent_active()
    await ctx.shuffle_into_deck(full_stack(chosen), ctx.opponent_id)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.opponent_id):
                screen = ctx.session.players[ctx.opponent_id].screen_name
                await ctx.session.end_game(
                    ctx.player_id, f"{screen} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="53921530-4314-5662-8d8c-45ab882e2267",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Reversing Gust",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Pok\u00e9mon. Shuffle that Pok\u00e9mon and all attached cards into their deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=flip_gate(_shuffle_a_defender_away),
        ),
        Attack(
            title="Perplex",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)