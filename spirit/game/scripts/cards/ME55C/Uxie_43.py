from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1b4d6a43-a09d-53be-b762-adea373c63e3",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Uxie.Name",
    display_name="Uxie",
    searchable_by=["Uxie", "Basic", "Uxie"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="ME55C",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=480,
    abilities=[
        Ability(
            title="Set Up",
            game_text="Once during your turn, when you put Uxie from your hand onto your Bench, you may draw cards until you have 7 cards in your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Restore",
            game_text="You may put Uxie and all cards attached to it on the bottom of your deck in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)