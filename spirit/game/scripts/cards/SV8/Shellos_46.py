from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2cb06aa9-4a9a-5417-9dc3-b172186491fd",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shellos.Name",
    display_name="Shellos",
    searchable_by=["Shellos", "Basic", "Shellos"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=422,
    abilities=[
        Attack(
            title="Sprinkle Water",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)