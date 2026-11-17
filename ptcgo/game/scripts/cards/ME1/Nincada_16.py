from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="21fd23a9-897b-5b95-a3f9-238662fdcc6f",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    display_name="Nincada",
    searchable_by=["Nincada", "Basic", "Nincada"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="ME1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=290,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)