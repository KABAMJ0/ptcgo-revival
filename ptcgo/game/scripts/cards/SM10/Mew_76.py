from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _spread_counters(ctx):
    await ctx.deal_damage()
    await ctx.place_damage_counters(3)


card = PokemonCardDef(
    guid="46e5bb52-b8f8-5f91-8e4e-be8cdfcb4074",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Bench Barrier",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon by your opponent's attacks.",
            effect=unimplemented,
        ),
        Attack(
            title="Psypower",
            game_text="Put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_spread_counters,
        ),
    ],
)