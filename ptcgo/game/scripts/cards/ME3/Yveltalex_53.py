from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def soul_destroyer(ctx):
    """Knock Out each opposing Pokemon with 50 HP or less remaining."""
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        if pokemon.get_attribute(AttrID.HP, 0) <= 50:
            await ctx.knock_out(pokemon)


card = PokemonCardDef(
    guid="913b2cae-eeec-51e8-9afd-8fdd4f31e8f3",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltalex.Name",
    display_name="Yveltal ex",
    searchable_by=["Yveltal ex", "Basic", "ex", "Yveltalex"],
    subtypes=["Basic", "ex"],
    collector_number=53,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=717,
    abilities=[
        Attack(
            title="Soul Destroyer",
            game_text="Knock Out each of your opponent's Pok\u00e9mon that has 50 HP or less remaining.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            effect=soul_destroyer,
        ),
        Attack(
            title="Dark Strike",
            game_text="During your next turn, this Pok\u00e9mon can't use Dark Strike.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=unimplemented,
        ),
    ],
)