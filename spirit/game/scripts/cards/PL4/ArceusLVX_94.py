from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1b1a2f8a-9d1a-54f0-b2ed-6beb4c7bc357",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusLVX.Name",
    display_name="Arceus LV.X",
    searchable_by=["Arceus LV.X", "Level-Up", "ArceusLVX"],
    subtypes=["Level-Up"],
    collector_number=94,
    set_code="PL4",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Arceus.Name",
    family_id=493,
    abilities=[
        Ability(
            title="Multi-type",
            game_text="Arceus LV. X's type is the same type as its previous Level.",
            effect=unimplemented,
        ),
        Ability(
            title="Omniscient",
            game_text="Arceus can use the attacks of all Arceus you have in play as its own. (You still need the necessary Energy to use each attack.)",
            effect=unimplemented,
        ),
    ],
)