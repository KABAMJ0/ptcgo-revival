from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack, count_energy


async def strength_sap(ctx):
    """Printed 30; heal 30 from this Pokemon for each Energy card on the
    opponent's Active."""
    await ctx.deal_damage()
    attached = count_energy("defender", cards=True)(ctx)
    if attached:
        await ctx.heal(30 * attached, ctx.attacker)


card = PokemonCardDef(
    guid="89424f26-d479-5184-b86e-5e18f7621dfa",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiinotic.Name",
    display_name="Shiinotic",
    searchable_by=["Shiinotic", "Stage 1", "Shiinotic"],
    subtypes=["Stage 1"],
    collector_number=98,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name",
    family_id=755,
    abilities=[
        Attack(
            title="Strength Sap",
            game_text="Heal from this Pok\u00e9mon 30 damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=strength_sap,
        ),
        Attack(
            title="Sleep Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)