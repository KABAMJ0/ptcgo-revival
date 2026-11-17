from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="024d71af-1e18-5a2b-ae8e-871ee0646b5d",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPorygon.Name",
    display_name="Team Rocket's Porygon",
    searchable_by=["Team Rocket's Porygon", "Basic", "TeamRocketsPorygon"],
    subtypes=["Basic"],
    collector_number=153,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=137,
    abilities=[
        Attack(
            title="Hacking",
            game_text="Discard a card from your hand. If you do, your opponent discards a card from their hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)