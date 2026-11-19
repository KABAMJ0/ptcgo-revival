from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def unruly_claw(ctx):
    """On evolve: you may discard an Energy attached to the opponent's
    Active Pokemon."""
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    if not await ctx.ask_yes_no(
        "Discard an Energy attached to your opponent's Active Pok\u00e9mon?"
    ):
        return
    await ctx.discard_energy_from(
        target, 1, prompt="Choose Energy to discard from the Defending Pok\u00e9mon")


card = PokemonCardDef(
    guid="ee940f97-1bfd-55f8-ac29-694e97b1bcef",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crawdaunt.Name",
    display_name="Crawdaunt",
    searchable_by=["Crawdaunt", "Stage 1", "Crawdaunt"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    family_id=341,
    abilities=[
        Ability(
            title="Unruly Claw",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=unruly_claw,
        ),
        Attack(
            title="Crabhammer",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)