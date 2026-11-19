from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.session.effects import full_stack


async def _shuffle_self_in(ctx):
    await ctx.deal_damage()
    await ctx.shuffle_into_deck(full_stack(ctx.attacker), ctx.player_id)
    if not await ctx.session._promote_new_active(ctx.player_id):
        screen = ctx.session.players[ctx.player_id].screen_name
        await ctx.session.end_game(
            ctx.opponent_id, f"{screen} has no Pokémon left"
        )


card = PokemonCardDef(
    guid="260ec245-10c0-597b-9b2f-ec5db27bab62",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lopunny.Name",
    display_name="Lopunny",
    searchable_by=["Lopunny", "Stage 1", "Lopunny"],
    subtypes=["Stage 1"],
    collector_number=107,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    family_id=427,
    abilities=[
        Attack(
            title="Stompy Stomp",
            game_text="Flip 2 coins. This attack does 40 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=40),
        ),
        Attack(
            title="Happy Turn",
            game_text="You may shuffle this Pok\u00e9mon and all cards attached to it into your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_shuffle_self_in,
        ),
    ],
)