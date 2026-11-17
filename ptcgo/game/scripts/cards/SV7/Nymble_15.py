from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b0110894-c1d3-5b47-97d7-be0f85f8d2d5",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name",
    display_name="Nymble",
    searchable_by=["Nymble", "Basic", "Nymble"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=919,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)