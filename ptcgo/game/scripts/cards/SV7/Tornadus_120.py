from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d8700bee-2e6a-5fb3-8dc9-ed2addafaaa7",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tornadus.Name",
    display_name="Tornadus",
    searchable_by=["Tornadus", "Basic", "Tornadus"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=641,
    abilities=[
        Attack(
            title="Knuckle Punch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Storm Barrier",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)