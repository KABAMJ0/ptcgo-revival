from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="21fcddc6-697c-5923-b9b1-3d7e21e78f49",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Comfey.Name",
    display_name="Comfey",
    searchable_by=["Comfey", "Basic", "Comfey"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=764,
    abilities=[
        Ability(
            title="Flower Shield",
            game_text="Each of your Pok\u00e9mon that has any Fairy Energy attached to it can't be affected by any Special Conditions. Remove any Special Conditions affecting those Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Sweet Kiss",
            game_text="Your opponent draws a card.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)