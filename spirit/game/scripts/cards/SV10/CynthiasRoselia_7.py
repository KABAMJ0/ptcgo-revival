from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9deb537c-60b0-5e3a-83c0-aebe7878afe5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasRoselia.Name",
    display_name="Cynthia's Roselia",
    searchable_by=["Cynthia's Roselia", "Basic", "CynthiasRoselia"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=315,
    abilities=[
        Attack(
            title="Spike Sting",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)