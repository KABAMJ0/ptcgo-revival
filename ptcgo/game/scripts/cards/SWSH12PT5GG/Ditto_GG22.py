from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3171c2d7-401e-5876-b368-848e7f289993",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Sudden Transformation",
            game_text="This Pok\u00e9mon can use the attacks of any Basic Pok\u00e9mon in your discard pile, except for Pok\u00e9mon with a Rule Box (Pok\u00e9mon V, Pok\u00e9mon-GX, etc. have Rule Boxes). (You still need the necessary Energy to use each attack.)",
            effect=unimplemented,
        ),
    ],
)