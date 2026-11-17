from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d8928363-c1ef-5d0f-b2c6-3f76d2f3ce7f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gholdengoex.Name",
    display_name="Gholdengo ex",
    searchable_by=["Gholdengo ex", "Stage 1", "ex", "Gholdengoex"],
    subtypes=["Stage 1", "ex"],
    collector_number=139,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    family_id=999,
    abilities=[
        Ability(
            title="Coin Bonus",
            game_text="Once during your turn, you may draw a card. If this Pok\u00e9mon is in the Active Spot, draw 1 more card.",
            effect=unimplemented,
        ),
        Attack(
            title="Make It Rain",
            game_text="Discard any number of Basic Energy cards from your hand. This attack does 50 damage for each card you discarded in this way.",
            cost={PokemonTypes.METAL: 1},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)