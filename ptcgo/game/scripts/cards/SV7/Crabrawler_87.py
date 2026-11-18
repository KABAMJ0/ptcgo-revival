from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="020d1538-9303-5643-8684-d2759d2c3fa6",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name",
    display_name="Crabrawler",
    searchable_by=["Crabrawler", "Basic", "Crabrawler"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=739,
    abilities=[
        Attack(
            title="Vise Grip",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Crabhammer",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)