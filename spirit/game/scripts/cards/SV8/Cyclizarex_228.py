from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3b44912a-d593-5ddb-b836-ebf739b730e4",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizarex.Name",
    display_name="Cyclizar ex",
    searchable_by=["Cyclizar ex", "Basic", "Tera", "ex", "Cyclizarex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=228,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=967,
    abilities=[
        Attack(
            title="Break Through",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=unimplemented,
        ),
        Attack(
            title="Zircon Road",
            game_text="You may draw 5 cards.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1},
            damage=180,
            effect=unimplemented,
        ),
    ],
)