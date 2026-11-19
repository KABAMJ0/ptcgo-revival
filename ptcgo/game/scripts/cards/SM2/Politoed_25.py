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
    guid="8c2c52cb-51c3-5da5-a799-f226be89032f",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Politoed.Name",
    display_name="Politoed",
    searchable_by=["Politoed", "Stage 2", "Politoed"],
    subtypes=["Stage 2"],
    collector_number=25,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=186,
    abilities=[
        Attack(
            title="Roll Call",
            game_text="Search your deck for a Poliwag, a Poliwhirl, and a Poliwrath, and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Hyper Jump",
            game_text="You may shuffle this Pok\u00e9mon and all cards attached to it into your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=_shuffle_self_in,
        ),
    ],
)