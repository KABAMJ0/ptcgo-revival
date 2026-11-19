from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import AttrID


async def _lightning_crush(ctx):
    results = await ctx.flip_coins(1, "Lightning Crush")
    if results and results[0]:
        await ctx.deal_damage(80)
        return
    await ctx.deal_damage(40)
    if ctx.defender is not None:
        await ctx.discard_energy_from(
            ctx.defender, 1, prompt="Discard an Energy attached to the Defending Pokémon")


def _conductivity_applies(ctx):
    return (ctx.attaching_player_id == ctx.opponent_id
            and ctx.energy_receiver is not None)


async def _conductivity(ctx):
    if _conductivity_applies(ctx):
        await ctx.deal_damage(10, target=ctx.energy_receiver, apply_modifiers=False,
                              as_counters=True)


card = PokemonCardDef(
    guid="4a96a396-bde5-5c0e-b8f0-fe1f8cc0785f",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2", "Prime", "Ampharos"],
    subtypes=["Stage 2", "Prime"],
    collector_number=105,
    set_code="HGSS1",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Conductivity",
            game_text="Whenever your opponent attaches an Energy card from his or her hand to 1 of his or her Pok\u00e9mon, put 1 damage counter on that Pok\u00e9mon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=unimplemented,
        ),
        Attack(
            title="Lightning Crush",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 40 more damage. If tails, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=_lightning_crush,
        ),
    ],
)