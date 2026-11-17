from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dc578eb4-9a59-5cd6-adbc-c5016da22a42",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SunnyCastform.Name",
    display_name="Sunny Castform",
    searchable_by=["Sunny Castform", "Basic", "SunnyCastform"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=351,
    abilities=[
        Ability(
            title="Temperamental Weather",
            game_text="Once during your turn (before your attack), you may search your deck for Castform, Rain Castform, or Snow-cloud Castform and switch it with Sunny Castform. (Any cards attached to Sunny Castform, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) Shuffle Sunny Castform back into your deck. You can't use more than 1 Temperamental Weather Pok\u00e9-Power each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Holon Search",
            game_text="Search your deck for a Holon Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)