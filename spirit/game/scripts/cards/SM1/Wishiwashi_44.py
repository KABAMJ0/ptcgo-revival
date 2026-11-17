from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c92aeed8-b72c-5f7c-b8e4-e9b21492e29b",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashi.Name",
    display_name="Wishiwashi",
    searchable_by=["Wishiwashi", "Basic", "Wishiwashi"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=746,
    abilities=[
        Ability(
            title="Cowardice",
            game_text="Once during your turn (before your attack), you may discard all cards attached to this Pok\u00e9mon and return it to your hand. You can't use this Ability during your first turn or on the turn this Pok\u00e9mon was put into play.",
            effect=unimplemented,
        ),
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)