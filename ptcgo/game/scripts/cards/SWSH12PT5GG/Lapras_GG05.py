from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

async def raging_freeze(ctx):
    """110 damage. If any of your Pokémon were KO'd by an opponent's attack
    last turn, your opponent's Active Pokémon is now Paralyzed."""
    await ctx.deal_damage()
    if ctx.kos_suffered_last_turn(ctx.player_id) > 0:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)

card = PokemonCardDef(
    guid="7bd93e35-b412-5541-b029-32367b26865e",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Attack(
            title="Raging Freeze",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an attack from your opponent's Pok\u00e9mon during their last turn, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=raging_freeze,
        ),
    ],
)