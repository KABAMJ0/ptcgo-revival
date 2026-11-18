from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4a550ce5-90a4-5e86-b377-65a83e519525",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name",
    display_name="Tadbulb",
    searchable_by=["Tadbulb", "Basic", "Tadbulb"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=938,
    abilities=[
        Attack(
            title="Stampede",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
        ),
    ],
)