from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b933d1c0-cf1f-564d-8c56-a67b2d02912c",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BronzongG.Name",
    display_name="Bronzong G",
    searchable_by=["Bronzong G", "Basic", "SP", "BronzongG"],
    subtypes=["Basic", "SP"],
    collector_number=41,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIRE,
    family_id=437,
    abilities=[
        Ability(
            title="Galactic Switch",
            game_text="Once during your turn (before your attack), you may move an Energy card attached to 1 of your Pok\u00e9mon SP to another of your Pok\u00e9mon. Then, put 2 damage counters on Bronzong G. This power can't be used if Bronzong G is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Pulse",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)