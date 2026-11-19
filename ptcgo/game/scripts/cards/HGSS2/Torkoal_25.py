from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import SpecialConditions


async def _hot_snort(ctx):
    results = await ctx.flip_coins(1, "Hot Snort")
    if results and results[0] and ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="3e0732b9-d233-565c-a7ac-8134cc1c2503",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name",
    display_name="Torkoal",
    searchable_by=["Torkoal", "Basic", "Torkoal"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="HGSS2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=324,
    abilities=[
        Ability(
            title="Hot Snort",
            game_text="Once during your turn, when you put Torkoal from your hand onto your Bench, you may flip a coin. If heads, the Defending Pok\u00e9mon is now Burned.",
            trigger=Triggers.ON_PLAY,
            effect=_hot_snort,
        ),
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)