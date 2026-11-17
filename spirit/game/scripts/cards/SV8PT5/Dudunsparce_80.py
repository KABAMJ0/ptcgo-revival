from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3c4265af-35ff-5da8-850c-0824e98ae182",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dudunsparce.Name",
    display_name="Dudunsparce",
    searchable_by=["Dudunsparce", "Stage 1", "Dudunsparce"],
    subtypes=["Stage 1"],
    collector_number=80,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name",
    family_id=206,
    abilities=[
        Ability(
            title="Run Away Draw",
            game_text="Once during your turn, you may draw 3 cards. If you drew any cards in this way, shuffle this Pok\u00e9mon and all attached cards into your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Land Crush",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)