from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype
from ptcgo.game.session.effects import full_stack


def _has_technical_machine(ctx):
    return any(pokemon is ctx.attacker and has_pokemon_subtype(tool, "Technical Machine")
               for tool, pokemon in ctx.tools_in_play())


async def _gripthrow(ctx):
    results = await ctx.flip_coins(1, "Gripthrow")
    if not (results and results[0]):
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.put_in_hand(full_stack(target), reveal=False)

    async def _promote():
        await ctx.session._promote_new_active(ctx.opponent_id)

    ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="f4c301af-f23c-5185-bfa6-fecaf8c2fe19",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crawdaunt.Name",
    display_name="Crawdaunt",
    searchable_by=["Crawdaunt", "Stage 1", "Crawdaunt"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    family_id=341,
    abilities=[
        Attack(
            title="Gripthrow",
            game_text="Flip a coin. If heads, your opponent returns the Defending Pok\u00e9mon and all cards attached to it to his or her hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=_gripthrow,
        ),
        Attack(
            title="Prop-up Pinchers",
            game_text="If Crawdaunt has a Technical Machine card attached to it, this attack does 50 damage plus 30 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_has_technical_machine, 30),
        ),
    ],
)