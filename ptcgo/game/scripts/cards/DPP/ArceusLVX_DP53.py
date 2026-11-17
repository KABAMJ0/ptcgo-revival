from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e9fbf3bc-3447-5abf-b961-431bdd4569f9",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusLVX.Name",
    display_name="Arceus LV.X",
    searchable_by=["Arceus LV.X", "Level-Up", "ArceusLVX"],
    subtypes=["Level-Up"],
    collector_number=53,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Arceus.Name",
    family_id=493,
    abilities=[
        Ability(
            title="Multitype",
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