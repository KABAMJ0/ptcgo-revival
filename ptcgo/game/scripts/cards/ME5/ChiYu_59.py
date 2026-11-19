from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_counters_on

async def whirling_envy(ctx):
    """20, plus 90 with 2 or more damage counters on this Pokemon; this
    attack's damage isn't affected by Weakness."""
    counters = damage_counters_on("self")(ctx)
    await ctx.deal_damage(20 + (90 if counters >= 2 else 0),
                          ignore_weakness=True)

async def whirling_envy(ctx):
    """20 base, +90 while this Pokemon carries 2 or more damage counters;
    the printed damage ignores Weakness."""
    hurt = len(ctx.attached_damage_counters(ctx.attacker)) >= 2 if hasattr(ctx, "attached_damage_counters") else False
    amount = 110 if hurt else 20
    await ctx.deal_damage(amount, ignore_weakness=True)


card = PokemonCardDef(
    guid="e46a2813-d9b5-5529-a986-51c44ad9dd20",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChiYu.Name",
    display_name="Chi-Yu",
    searchable_by=["Chi-Yu", "Basic", "ChiYu"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=1004,
    abilities=[
        Attack(
            title="Whirling Envy",
            game_text="If this Pok\u00e9mon has 2 or more damage counters on it, this attack does 90 more damage. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="+",
            effect=whirling_envy,
        ),
    ],
)