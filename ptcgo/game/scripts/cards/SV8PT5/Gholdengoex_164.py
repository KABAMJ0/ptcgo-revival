from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cdb67b4c-30c3-5095-b637-698e063c5abd",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gholdengoex.Name",
    display_name="Gholdengo ex",
    searchable_by=["Gholdengo ex", "Stage 1", "ex", "Gholdengoex"],
    subtypes=["Stage 1", "ex"],
    collector_number=164,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    family_id=1000,
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