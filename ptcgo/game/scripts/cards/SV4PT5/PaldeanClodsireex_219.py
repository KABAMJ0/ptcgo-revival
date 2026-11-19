from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import lock_all_attacks


async def poisonous_puddle(ctx):
    """Once during your turn, if a Stadium is in play, you may make your
    opponent's Active Pokemon Poisoned."""
    if await ctx.ask_yes_no("Make your opponent's Active Pokémon Poisoned?"):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


def _stadium_in_play_condition(board, player_id, pokemon):
    area = board.find_global_area("activeStadium")
    return bool(area and area.children)


async def white_blaze(ctx):
    """Flip a coin. If tails, during your next turn, this Pokémon can't attack."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, ctx.ability.title))[0]
    if not heads:
        lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="9c1c3475-f8b4-5cfc-87b0-65e9100ca9a3",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanClodsireex.Name",
    display_name="Paldean Clodsire ex",
    searchable_by=["Paldean Clodsire ex", "Stage 1", "ex", "PaldeanClodsireex"],
    subtypes=["Stage 1", "ex"],
    collector_number=219,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name",
    family_id=194,
    abilities=[
        Ability(
            title="Toxic Wetland",
            game_text="Once during your turn, if a Stadium is in play, you may make your opponent's Active Pok\u00e9mon Poisoned.",
            activation=Activations.ONCE_PER_TURN,
            condition=_stadium_in_play_condition,
            effect=poisonous_puddle,
        ),
        Attack(
            title="Needle Bone",
            game_text="Flip a coin. If tails, during your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=white_blaze,
        ),
    ],
)