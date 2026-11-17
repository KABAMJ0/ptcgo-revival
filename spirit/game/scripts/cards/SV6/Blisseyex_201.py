from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="68ff8c9d-660d-5b3c-b2da-dbb579f07a30",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blisseyex.Name",
    display_name="Blissey ex",
    searchable_by=["Blissey ex", "Stage 1", "ex", "Blisseyex"],
    subtypes=["Stage 1", "ex"],
    collector_number=201,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=113,
    abilities=[
        Ability(
            title="Happy Switch",
            game_text="Once during your turn, you may move a Basic Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Return",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=unimplemented,
        ),
    ],
)