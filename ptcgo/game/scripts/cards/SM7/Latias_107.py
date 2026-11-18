from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ed5d024d-0e2c-5d1c-bde9-540046b533a4",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias ◇",
    searchable_by=["Latias \u25c7", "Basic", "Prism Star", "Latias"],
    subtypes=["Basic", "Prism Star"],
    collector_number=107,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=380,
    abilities=[
        Attack(
            title="Dreamy Mist",
            game_text="Attach a basic Energy card from your discard pile to each of your Basic Benched Dragon Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)