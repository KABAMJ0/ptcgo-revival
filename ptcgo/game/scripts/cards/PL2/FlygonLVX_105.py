from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a77daf80-dbe4-5c70-8eab-3e8d5cc0b5a6",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlygonLVX.Name",
    display_name="Flygon LV.X",
    searchable_by=["Flygon LV.X", "Level-Up", "FlygonLVX"],
    subtypes=["Level-Up"],
    collector_number=105,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Wind Erosion",
            game_text="As long as Flygon is your Active Pok\u00e9mon, discard the top card from your opponent's deck between turns.",
            effect=unimplemented,
        ),
        Attack(
            title="Extreme Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon LV.X. This attack does 150 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon).",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)