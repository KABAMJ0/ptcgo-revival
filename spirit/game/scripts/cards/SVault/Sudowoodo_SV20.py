from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0e2ba384-a973-52f1-8865-8ae8af777779",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic", "Sudowoodo"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=185,
    abilities=[
        Ability(
            title="Roadblock",
            game_text="Your opponent can't have more than 4 Benched Pok\u00e9mon. If they have 5 or more Benched Pok\u00e9mon, they discard Benched Pok\u00e9mon until they have 4 Pok\u00e9mon on the Bench. If more than one effect changes the number of Benched Pok\u00e9mon allowed, use the smaller number.",
            effect=unimplemented,
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)