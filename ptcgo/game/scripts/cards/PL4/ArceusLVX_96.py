from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8f4d6fc2-080f-5a31-9fa5-7e9bf726f007",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusLVX.Name",
    display_name="Arceus LV.X",
    searchable_by=["Arceus LV.X", "Level-Up", "ArceusLVX"],
    subtypes=["Level-Up"],
    collector_number=96,
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
            title="Multitype",
            game_text="Arceus LV.X's type is the same type as its previous Level.",
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Bolt",
            game_text="Discard a Lightning Energy and a Psychic Energy attached to Arceus.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)