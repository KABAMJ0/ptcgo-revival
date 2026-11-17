from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e29a5d09-68a4-5860-8c0f-e661dc3f7b50",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name",
    display_name="Nymble",
    searchable_by=["Nymble", "Basic", "Nymble"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    family_id=919,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)