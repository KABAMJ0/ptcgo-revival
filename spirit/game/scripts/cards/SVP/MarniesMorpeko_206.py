from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0de8c3c1-d979-54d1-831b-f86b86f696e6",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesMorpeko.Name",
    display_name="Marnie's Morpeko",
    searchable_by=["Marnie's Morpeko", "Basic", "MarniesMorpeko"],
    subtypes=["Basic"],
    collector_number=206,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    family_id=877,
    abilities=[
        Attack(
            title="Spiky Wheel",
            game_text="This attack does 40 more damage for each Darkness Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)