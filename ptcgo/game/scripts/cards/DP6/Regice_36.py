from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ea1646f9-88d9-5cdf-b63c-df3d4bb93c86",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regice.Name",
    display_name="Regice",
    searchable_by=["Regice", "Basic", "Regice"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=378,
    abilities=[
        Ability(
            title="Regi Move",
            game_text="Once during your turn (before your attack), you may use this power. Discard 2 cards from your hand and choose 1 of your opponent's Active Pok\u00e9mon that isn't an Evolved Pok\u00e9mon. Then, your opponent switches that Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon. This power can't be used if Regice is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Ice Reflect",
            game_text="If Regice was damaged by an attack during your opponent's last turn, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)