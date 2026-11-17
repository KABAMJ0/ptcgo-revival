from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1a1d7785-52c9-5804-8408-2f6635b8eeb9",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlazikenFBLVX.Name",
    display_name="Blaziken FB LV.X",
    searchable_by=["Blaziken FB LV.X", "Level-Up", "SP", "BlazikenFBLVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=142,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlazikenFB.Name",
    family_id=257,
    abilities=[
        Ability(
            title="Burning Spirit",
            game_text="Any damage done by attacks to a Burned Pok\u00e9mon (both yours and your opponent's) is increased by 40 (after applying Weakness and Resistance). No more than 40 damage can be added by all Burning Spirit Pok\u00e9-Bodies.",
            effect=unimplemented,
        ),
        Attack(
            title="Jet Shoot",
            game_text="During your opponent's next turn, any damage done to Blaziken FB by attacks is increased by 40 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)