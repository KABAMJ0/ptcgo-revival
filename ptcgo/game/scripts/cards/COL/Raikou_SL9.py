from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def raging_thunder(ctx):
    """Printed 70, then 20 to 1 of your own Pokemon with no Weakness or
    Resistance on that hit."""
    await ctx.deal_damage()
    mine = [p for p in ctx.my_pokemon_in_play() if p is not None]
    if not mine:
        return
    target = await ctx.choose_pokemon(mine, "Choose 1 of your Pokemon to take 20")
    if target is not None:
        await ctx.deal_damage(20, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="38dc39e8-48d4-5e70-8a49-3f3eb9714f46",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou",
    searchable_by=["Raikou", "Basic", "Raikou"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="COL",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=243,
    abilities=[
        Ability(
            title="Extreme Speed",
            game_text="Raikou's Retreat Cost is Colorless less for each Lightning Energy attached to Raikou.",
            effect=unimplemented,
        ),
        Attack(
            title="Raging Thunder",
            game_text="Does 20 damage to 1 of your Pok\u00e9mon and don't apply Weakness and Resistance to this damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=raging_thunder,
        ),
    ],
)