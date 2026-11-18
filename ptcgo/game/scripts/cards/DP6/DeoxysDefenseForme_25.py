from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f786e788-3c84-5322-a361-71e8f47f23f4",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysDefenseForme.Name",
    display_name="Deoxys Defense Forme",
    searchable_by=["Deoxys Defense Forme", "Basic", "DeoxysDefenseForme"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Ability(
            title="Form Change",
            game_text="Once during your turn (before your attack), you may search your deck for any Deoxys and switch it with Deoxys Defense Forme. (Any cards attached to Deoxys Defense Forme, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) If you do, put Deoxys Defense Forme on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Pok\u00e9-Power each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Defense",
            game_text="During your opponent's next turn, prevent all effects of an attack, and any damage done to Deoxys by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)