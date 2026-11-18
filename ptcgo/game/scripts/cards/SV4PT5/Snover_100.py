from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="93298987-ca8c-517d-82fe-a11b28e02969",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    display_name="Snover",
    searchable_by=["Snover", "Basic", "Snover"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=459,
    abilities=[
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)