from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9fd8b516-ac7a-5f9d-b462-3795892019e0",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxysex.Name",
    display_name="Deoxys ex",
    searchable_by=["Deoxys ex", "Basic", "ex", "Deoxysex"],
    subtypes=["Basic", "ex"],
    collector_number=98,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Ability(
            title="Form Change",
            game_text="Once during your turn (before your attack), you may search your deck for another Deoxys ex and switch it with Deoxys ex. (Any cards attached to Deoxys ex, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) If you do, put Deoxys ex on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Pok\u00e9-Power each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Psyburst",
            game_text="You may discard 2 Energy attached to Deoxys ex. If you do, this attack does 50 damage plus 20 more damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)