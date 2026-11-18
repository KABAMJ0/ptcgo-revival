from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="62782593-fb01-574b-8fbc-fe20a14a2f4a",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minior.Name",
    display_name="Minior",
    searchable_by=["Minior", "Basic", "Minior"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=774,
    abilities=[
        Ability(
            title="Falling Star",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your hand and your Bench isn't full, you may move your Active Pok\u00e9mon to your Bench and play this Pok\u00e9mon as your new Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)