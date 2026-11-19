from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.session.effects import full_stack, is_special_energy
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
async def slice_off(ctx):
    """When played onto the Bench: discard a Special Energy from 1 of the
    opponent's Pokemon."""
    candidates = [p for p in ctx.opponent_pokemon_in_play()
                  if any(is_special_energy(e) for e in ctx.attached_energies(p))]
    if not candidates:
        return
    if not await ctx.ask_yes_no(
            "Discard a Special Energy from 1 of your opponent's Pokémon?"):
        return
    target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
        candidates, "Choose a Pokémon to discard a Special Energy from")
    if target is not None:
        await ctx.discard_energy_from(
            target, 1, predicate=is_special_energy,
            prompt="Choose a Special Energy to discard")


async def blade_gx(ctx):
    """Take a Prize card."""
    await ctx.take_prizes(1)


async def _shuffle_self_in(ctx):
    await ctx.deal_damage()
    await ctx.shuffle_into_deck(full_stack(ctx.attacker), ctx.player_id)
    if not await ctx.session._promote_new_active(ctx.player_id):
        screen = ctx.session.players[ctx.player_id].screen_name
        await ctx.session.end_game(
            ctx.opponent_id, f"{screen} has no Pokémon left"
        )


card = PokemonCardDef(
    guid="24f6a559-6d7d-5c7a-b6f4-a8c7498d1ae6",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KartanaGX.Name",
    display_name="Kartana-GX",
    searchable_by=["Kartana-GX", "Basic", "GX", "Ultra Beast", "KartanaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=117,
    set_code="SM4",
    rarity=Rarities.RareRainbow,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=798,
    abilities=[
        Ability(
            title="Slice Off",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may discard a Special Energy from 1 of your opponent's Pok\u00e9mon.",
            trigger=Triggers.ON_PLAY,
            effect=slice_off,
        ),
        Attack(
            title="Gale Blade",
            game_text="You may shuffle this Pok\u00e9mon and all cards attached to it into your deck.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_shuffle_self_in,
        ),
        Attack(
            title="Blade-GX",
            game_text="Take a Prize card. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 1},
            effect=blade_gx,
        ),
    ],
)