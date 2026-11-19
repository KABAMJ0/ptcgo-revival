from ptcgo.game.card_effects.support_common import remove_self_from_play
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.session.effects import full_stack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _shuffle_self_in(ctx):
    await ctx.deal_damage()
    await ctx.shuffle_into_deck(full_stack(ctx.attacker), ctx.player_id)
    if not await ctx.session._promote_new_active(ctx.player_id):
        screen = ctx.session.players[ctx.player_id].screen_name
        await ctx.session.end_game(
            ctx.opponent_id, f"{screen} has no Pokémon left"
        )


card = PokemonCardDef(
    guid="a6dc3316-048f-5078-86c1-2d19df322953",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KartanaGX.Name",
    display_name="Kartana-GX",
    searchable_by=["Kartana-GX", "Basic", "GX", "Ultra Beast", "KartanaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=73,
    set_code="SVault",
    rarity=Rarities.Rare,
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
            effect=unimplemented,
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
            effect=unimplemented,
        ),
    ],
)