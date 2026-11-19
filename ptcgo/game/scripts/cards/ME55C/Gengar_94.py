from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _spread_counters(ctx):
    await ctx.deal_damage()
    await ctx.place_damage_counters(4)


card = PokemonCardDef(
    guid="1fb0b000-59d0-5074-aba9-070f6d2933dc",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=94,
    set_code="ME55C",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=94,
    abilities=[
        Ability(
            title="Catastrophe",
            game_text="As long as Gengar is your Active Pok\u00e9mon, if any of your opponent's Pok\u00e9mon would be Knocked Out, put that Pok\u00e9mon in the Lost Zone instead of discarding. (Discard all cards attached to that Pok\u00e9mon.)",
            effect=unimplemented,
        ),
        Attack(
            title="Hurl into Darkness",
            game_text="Look at your opponent's hand and choose a number of Pok\u00e9mon you find there up to the number of Psychic Energy attached to Gengar. Put the Pok\u00e9mon you chose in the Lost Zone.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Cursed Drop",
            game_text="Put 4 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=_spread_counters,
        ),
    ],
)