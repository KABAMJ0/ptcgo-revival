from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5d53564d-4288-5b3a-b351-ffec793e9c5c",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name",
    display_name="Paldean Wooper",
    searchable_by=["Paldean Wooper", "Basic", "PaldeanWooper"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=194,
    abilities=[
        Attack(
            title="Splattering Poison",
            game_text="Both Active Pok\u00e9mon are now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)