from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

async def _paralyzing_hit(ctx):
    """Printed damage, then one coin: heads Paralyzes the defender and discards
    an Energy from it. One flip covers both halves, as the card prints it."""
    await ctx.deal_damage()
    if not (await ctx.flip_coins(1))[0]:
        return
    defender = ctx.defender
    if defender is None:
        return
    if not ctx.effects_blocked(defender):
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
    if ctx.attached_energies(defender):
        await ctx.discard_energy_from(defender, 1)

card = PokemonCardDef(
    guid="47beaee1-765e-5f0f-bc44-8422dc2c5371",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glalie.Name",
    display_name="Glalie",
    searchable_by=["Glalie", "Stage 1", "Glalie"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Attack(
            title="Ice Fang",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed, and discard an Energy from that Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=_paralyzing_hit,
        ),
        Attack(
            title="Frosty Typhoon",
            game_text="This Pok\u00e9mon can't use Frosty Typhoon during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)