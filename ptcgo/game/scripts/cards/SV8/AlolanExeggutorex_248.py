from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="78da55bd-894b-5717-982d-ef93783616aa",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutorex.Name",
    display_name="Alolan Exeggutor ex",
    searchable_by=["Alolan Exeggutor ex", "Stage 1", "Tera", "ex", "AlolanExeggutorex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=248,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Tropical Frenzy",
            game_text="You may attach any number of Basic Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1},
            damage=150,
            effect=unimplemented,
        ),
        Attack(
            title="Swinging Sphene",
            game_text="Flip a coin. If heads, Knock Out your opponent's Active Basic Pok\u00e9mon. If tails, Knock Out 1 of your opponent's Benched Basic Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            effect=unimplemented,
        ),
    ],
)