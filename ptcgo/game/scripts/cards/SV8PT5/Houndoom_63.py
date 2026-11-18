from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="38fdc7b8-d63c-5c78-b876-a95862854c91",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Houndoom"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Call to Muster",
            game_text="Search your deck for up to 2 Basic Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Pitch-Black Fangs",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)