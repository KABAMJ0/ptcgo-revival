from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5e012081-7cfb-5877-8b3a-e81f91aac685",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    display_name="Applin",
    searchable_by=["Applin", "Basic", "Applin"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=840,
    abilities=[
        Attack(
            title="Withdraw",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)