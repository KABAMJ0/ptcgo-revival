from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.attacks_common import named_in_play
from ptcgo.game.card_effects.passives_common import apply_protection

async def super_fast(ctx):
    """30; with Pachirisu in play a heads stops everything the next attack would
    do to Buizel."""
    await ctx.deal_damage(30)
    if not named_in_play("Pachirisu")(ctx):
        return
    results = await ctx.flip_coins(1, "Super Fast")
    if results and results[0]:
        await apply_protection(ctx, target=ctx.attacker, prevent=True,
                               effects_too=True)

card = PokemonCardDef(
    guid="e66125e7-bae4-579a-a10f-6f090c6bf956",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name",
    display_name="Buizel",
    searchable_by=["Buizel", "Basic", "Buizel"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="POP9",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=418,
    abilities=[
        Attack(
            title="Whirlpool",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=flip_gate(discard_opponent_energy_attack(1)),
        ),
        Attack(
            title="Super Fast",
            game_text="If you have Pachirisu in play, flip a coin. If heads, prevent all effects of an attack, including damage, done to Buizel during your opponent's next turn.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=super_fast,
        ),
    ],
)