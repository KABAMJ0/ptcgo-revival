from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _spread_counters(ctx):
    await ctx.deal_damage()
    await ctx.place_damage_counters(3)


card = PokemonCardDef(
    guid="db469a57-d491-53e7-9e7b-79c75df1dee6",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    display_name="Lampent",
    searchable_by=["Lampent", "Stage 1", "Lampent"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Cursed Drop",
            game_text="Put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_spread_counters,
        ),
        Attack(
            title="Night March",
            game_text="This attack does 20 damage times the number of Pok\u00e9mon in your discard pile that have the Night March attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)