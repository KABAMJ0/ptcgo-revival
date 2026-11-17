from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5f96ac76-2c2b-5422-b71c-1ddaa1acdc1d",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardGLVX.Name",
    display_name="Charizard G LV.X",
    searchable_by=["Charizard G LV.X", "Level-Up", "SP", "CharizardGLVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=143,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardG.Name",
    family_id=6,
    abilities=[
        Ability(
            title="Call for Power",
            game_text="As often as you like during your turn (before your attack), you may move an Energy attached to 1 of your Pok\u00e9mon to Charizard G. This power can't be used if Charizard G is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Malevolent Fire",
            game_text="Flip a coin. If tails, discard all Energy attached to Charizard G.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=unimplemented,
        ),
    ],
)