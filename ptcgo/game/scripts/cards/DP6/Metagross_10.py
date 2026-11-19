from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations
from ptcgo.game.card_effects.passives_common import apply_own_next_turn_boost


async def _magnetic_reversal(ctx):
    """Magnetic Reversal: heads pulls their Benched Pokemon into the Active."""
    heads = await ctx.flip_coins(1, "Magnetic Reversal")
    if not (heads and all(heads)):
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokemon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


async def _extra_comet_punch(ctx):
    """Extra Comet Punch: next turn's base damage is 100 rather than 50."""
    await ctx.deal_damage()
    await apply_own_next_turn_boost(
        ctx, 100 - (getattr(ctx.ability, "damage", 0) or 0),
        attack_title="Extra Comet Punch")

card = PokemonCardDef(
    guid="dfcc1af4-badb-5f35-a338-464dde644afd",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Magnetic Reversal",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, switch 1 of your opponent's Benched Pok\u00e9mon with 1 of the Defending Pok\u00e9mon. This power can't be used if Metagross is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=lambda board, player_id, pokemon: not pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS),
            effect=_magnetic_reversal,
        ),
        Attack(
            title="Extra Comet Punch",
            game_text="During your next turn, Metagross's Extra Comet Punch attack's base damage is 100.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=_extra_comet_punch,
        ),
    ],
)