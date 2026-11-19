from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _spread(ctx):
    """Printed damage, then N damage counters placed across the opponent's side."""
    await ctx.deal_damage()
    await ctx.place_damage_counters(3)


async def _spread_counters(ctx):
    await ctx.deal_damage()
    await ctx.place_damage_counters(4)

card = PokemonCardDef(
    guid="12d211bd-ca32-5eda-a78d-dbeca413377e",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=122,
    abilities=[
        Ability(
            title="Mimic Barrier",
            game_text="If this Pok\u00e9mon and your opponent's Active Pok\u00e9mon have the same amount of Energy attached, prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon.",
            effect=_spread,
        ),
        Attack(
            title="Psypower",
            game_text="Put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_spread_counters,
        ),
    ],
)