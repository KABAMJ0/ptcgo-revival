from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="36cf5825-57e9-5d09-bef5-ea64271aa899",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DittoVMAX.Name",
    display_name="Ditto VMAX",
    searchable_by=["Ditto VMAX", "VMAX", "DittoVMAX"],
    subtypes=["VMAX"],
    collector_number=119,
    set_code="SWSH45SV",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DittoV.Name",
    family_id=132,
    abilities=[
        Attack(
            title="Max Transform",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)