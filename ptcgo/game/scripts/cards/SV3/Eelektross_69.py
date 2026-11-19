from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.support_common import gust_then


def _paralyze_flip(pokemon):
    """flip_gate rider: heads Paralyzes the Pokemon switched in."""
    async def rider(ctx):
        await ctx.apply_special_condition(pokemon, SpecialConditions.PARALYZED)
    return flip_gate(rider)


async def _suction_shock(ctx, new_active):
    """60 to the new Active, then a coin flip for Paralysis on that Pokemon."""
    await ctx.deal_damage(60, target=new_active)
    await _paralyze_flip(new_active)(ctx)


card = PokemonCardDef(
    guid="ef1c6a9b-7e29-5abc-b226-20d87cf1c5a7",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektross.Name",
    display_name="Eelektross",
    searchable_by=["Eelektross", "Stage 2", "Eelektross"],
    subtypes=["Stage 2"],
    collector_number=69,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    family_id=602,
    abilities=[
        Attack(
            title="Suction Shock",
            game_text="Switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot. If you do, this attack does 60 damage to the new Active Pok\u00e9mon, and then flip a coin. If heads, that Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=gust_then(_suction_shock),
        ),
        Attack(
            title="Head Bolt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
        ),
    ],
)
