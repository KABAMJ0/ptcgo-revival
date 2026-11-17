from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="706eb983-a11f-570d-8687-95444cd57006",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name",
    display_name="Flabébé",
    searchable_by=["Flab\u00e9b\u00e9", "Basic", "Flabb"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=669,
    abilities=[
        Attack(
            title="Pollen Shot",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)