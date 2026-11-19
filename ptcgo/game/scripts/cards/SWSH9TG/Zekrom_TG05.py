from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

async def wild_shock(ctx):
    """130 damage; this Pokémon also does 60 damage to itself; opponent's Active is now Paralyzed."""
    await ctx.deal_damage()
    await ctx.deal_damage(60, target=ctx.attacker, apply_modifiers=False)
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)

card = PokemonCardDef(
    guid="950ffd37-7268-52c6-bd50-68e3f4661076",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zekrom.Name",
    display_name="Zekrom",
    searchable_by=["Zekrom", "Basic", "Zekrom"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SWSH9TG",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=644,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Wild Shock",
            game_text="This Pok\u00e9mon also does 60 damage to itself. Your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=wild_shock,
        ),
    ],
)