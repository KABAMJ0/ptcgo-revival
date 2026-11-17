from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="40feea7e-d3bc-5224-9729-68201a290704",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ElectivireFBLVX.Name",
    display_name="Electivire FB LV.X",
    searchable_by=["Electivire FB LV.X", "Level-Up", "SP", "ElectivireFBLVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=144,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ElectivireFB.Name",
    family_id=466,
    abilities=[
        Ability(
            title="Energy Recycle",
            game_text="Once during your turn (before your attack), you may use this power. If you do, your turn ends. Search your discard pile for up to 3 Energy cards and attach them to your Pok\u00e9mon in any way you like. This power can't be used if Electivire FB is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Powerful Spark",
            game_text="This attack does 30 damage plus 10 more damage for each Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)