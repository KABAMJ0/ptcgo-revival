from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8510a686-b19e-55aa-b827-c92874bde59d",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=132,
    abilities=[
        Ability(
            title="Duplicate",
            game_text="Once during your turn (before your attack), you may search your deck for another Ditto and switch it with Ditto. (Any cards attached to Ditto, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) If you do, put Ditto on top of your deck. Shuffle your deck afterward. You can't use more than 1 Duplicate Pok\u00e9-Power each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Toxic",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Put 2 damage counters instead of 1 on the Defending Pok\u00e9mon between turns.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)