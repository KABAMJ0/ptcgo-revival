from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _spread_counters(ctx):
    await ctx.deal_damage()
    await ctx.place_damage_counters(4)


card = PokemonCardDef(
    guid="45732293-ce7a-535d-8272-718247a77104",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChandelureEX.Name",
    display_name="Chandelure-EX",
    searchable_by=["Chandelure-EX", "Basic", "EX", "ChandelureEX"],
    subtypes=["Basic", "EX"],
    collector_number=77,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    family_id=609,
    abilities=[
        Attack(
            title="Cursed Drop",
            game_text="Put 4 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_spread_counters,
        ),
        Attack(
            title="Eerie Glow",
            game_text="The Defending Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)