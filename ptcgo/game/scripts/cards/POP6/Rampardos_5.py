from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def hasty_headbutt(ctx):
    """100 unaffected by Weakness, Resistance or any effect on the defender,
    then 20 to Rampardos itself."""
    await ctx.deal_damage(100, apply_modifiers=False, ignore_target_effects=True)
    if ctx.attacker is not None:
        await ctx.deal_damage(20, target=ctx.attacker, apply_modifiers=False)
card = PokemonCardDef(
    guid="6f4fac75-ea6a-5e96-930b-cf39149836bf",
    key="POP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rampardos.Name",
    display_name="Rampardos",
    searchable_by=["Rampardos", "Stage 2", "Rampardos"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="POP6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name",
    family_id=409,
    abilities=[
        Attack(
            title="Assurance",
            game_text="As long as the Defending Pok\u00e9mon's remaining HP is 60 or less, this attack's base damage is 60 instead of 30.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Hasty Headbutt",
            game_text="Rampardos does 20 damage to itself. This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=100,
            effect=hasty_headbutt,
        ),
    ],
)