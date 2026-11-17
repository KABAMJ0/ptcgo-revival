from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="70d82faf-af23-512a-b6fb-339415a5da38",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    display_name="Milcery",
    searchable_by=["Milcery", "Basic", "Milcery"],
    subtypes=["Basic"],
    collector_number=152,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=868,
    abilities=[
        Attack(
            title="Mumble",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)