from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6b30e855-d020-5d7d-9099-6d4373f78ac6",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TogekissC.Name",
    display_name="Togekiss C",
    searchable_by=["Togekiss C", "Basic", "SP", "TogekissC"],
    subtypes=["Basic", "SP"],
    collector_number=86,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=468,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Reckless Charge",
            game_text="Togekiss C does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)