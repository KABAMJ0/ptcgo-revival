from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="95008dfe-875a-505d-badd-db8fdaa8a0ba",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bramblin.Name",
    display_name="Bramblin",
    searchable_by=["Bramblin", "Basic", "Bramblin"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=946,
    abilities=[
        Attack(
            title="Spike Sting",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)