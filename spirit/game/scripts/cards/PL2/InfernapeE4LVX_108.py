from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b416a1fb-7d3c-5a68-95b5-8c199f1fee5c",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.InfernapeE4LVX.Name",
    display_name="Infernape E4 LV.X",
    searchable_by=["Infernape E4 LV.X", "Level-Up", "SP", "InfernapeE4LVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=108,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.InfernapeE4.Name",
    family_id=392,
    abilities=[
        Ability(
            title="Intimidating Roar",
            game_text="Once during your turn (before your attack), you may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon. This power can't be used if Infernape E4 is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Energy attached to Infernape E4.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)