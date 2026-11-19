from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, \
    Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import self_knockout


async def slap_of_misfortune(ctx):
    """70 damage; every coin the opponent flips next turn lands tails."""
    await ctx.deal_damage()
    ctx.lock_coin_flips()


async def six_feet_under(ctx):
    """Knock this Pokemon Out, then spread 3 damage counters over the
    opponent's Pokemon however the player likes."""
    if not await ctx.ask_yes_no("Knock Out this Pok\u00e9mon?"):
        return
    if not await self_knockout(ctx):
        return
    await ctx.place_damage_counters(3)

card = PokemonCardDef(
    guid="c1fc68e0-bf75-58f5-b996-62812748985a",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cofagrigus.Name",
    display_name="Cofagrigus",
    searchable_by=["Cofagrigus", "Stage 1", "Team Plasma", "Cofagrigus"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=56,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    family_id=562,
    abilities=[
        Ability(
            title="Six Feet Under",
            game_text="Once during your turn (before your attack) you may Knock Out this Pok\u00e9mon. If you do, put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            activation=Activations.ONCE_PER_TURN,
            effect=six_feet_under,
        ),
        Attack(
            title="Slap of Misfortune",
            game_text="Whenever your opponent flips a coin during his or her next turn, treat it as tails.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=slap_of_misfortune,
        ),
    ],
)