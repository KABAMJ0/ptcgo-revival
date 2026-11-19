from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card


async def energizing_sketch(ctx):
    """Flip 3 coins, then attach up to that many Basic Energy from the discard
    pile to your Benched Pokemon, distributed as you like."""
    flips = await ctx.flip_coins(3, "Energizing Sketch")
    heads = sum(1 for flip in flips or [] if flip)
    if heads <= 0 or not ctx.my_bench():
        return
    await attach_from_discard(
        is_basic_energy_card, count=heads, minimum=0,
        target=lambda pokemon: not is_in_active_spot(pokemon),
        distribute=True,
        prompt="Choose Basic Energy cards from your discard pile to attach",
    )(ctx)


card = PokemonCardDef(
    guid="18abdd49-6e15-5339-8607-b1f976871236",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle",
    searchable_by=["Smeargle", "Basic", "Smeargle"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="ME2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=235,
    abilities=[
        Attack(
            title="Energizing Sketch",
            game_text="Flip 3 coins. Attach an amount of Basic Energy up to the number of heads from your discard pile to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=energizing_sketch,
        ),
        Attack(
            title="Hook",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)