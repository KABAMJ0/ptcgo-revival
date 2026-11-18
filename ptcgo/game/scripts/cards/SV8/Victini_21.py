from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ea091398-4b0f-553d-8aa2-bda9cd5d2448",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic", "Victini"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Ability(
            title="Victory Cheer",
            game_text="Attacks used by your Evolution Fire Pok\u00e9mon do 10 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)