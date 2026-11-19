from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_choice

from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def flames_of_rage(ctx):
    """Discard 2 Fire Energy from Arcanine, then 40 plus 10 per damage counter
    on Arcanine."""
    await ctx.discard_energy_from(
        ctx.attacker, 2,
        predicate=lambda card: energy_provides_type(card, PokemonTypes.FIRE.value),
        prompt="Discard 2 Fire Energy attached to Arcanine")
    await damage_per(damage_counters_on("self"), 10, base=40)(ctx)

card = PokemonCardDef(
    guid="c7635583-6923-511f-99ca-4fb9b4e313d7",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1", "Arcanine"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=59,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_choice(heads=30, tails=10),
        ),
        Attack(
            title="Flames of Rage",
            game_text="Discard 2 Fire Energy cards attached to Arcanine in order to use this attack. This attack does 40 damage plus 10 more damage for each damage counter on Arcanine.",
            cost={PokemonTypes.FIRE: 2},
            damage=40,
            damage_operator="+",
            effect=flames_of_rage,
        ),
    ],
)