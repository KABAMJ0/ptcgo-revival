from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5a3859fd-04c4-531b-8523-0558c975060a",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminLVX.Name",
    display_name="Shaymin LV.X",
    searchable_by=["Shaymin LV.X", "Level-Up", "ShayminLVX"],
    subtypes=["Level-Up"],
    collector_number=127,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    family_id=492,
    abilities=[
        Ability(
            title="Revenge Seed",
            game_text="If any of your Grass Pok\u00e9mon were Knocked Out by damage from an opponent's attack during his or her last turn, each of Shaymin's attacks does 60 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Flare",
            game_text="You may move any number of Energy cards attached to your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)