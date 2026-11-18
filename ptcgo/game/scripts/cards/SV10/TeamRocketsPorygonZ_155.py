from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e63c51f5-90f4-5753-9740-09d9c2883ab3",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPorygonZ.Name",
    display_name="Team Rocket's Porygon-Z",
    searchable_by=["Team Rocket's Porygon-Z", "Stage 2", "TeamRocketsPorygonZ"],
    subtypes=["Stage 2"],
    collector_number=155,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPorygon2.Name",
    family_id=137,
    abilities=[
        Ability(
            title="Reconstitute",
            game_text="You must discard 2 cards from your hand in order to use this Ability. Once during your turn, you may draw a card.",
            effect=unimplemented,
        ),
        Attack(
            title="R Command",
            game_text="This attack does 20 damage for each Supporter card that has \"Team Rocket\" in its name in your discard pile.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)