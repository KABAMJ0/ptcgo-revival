from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1029edbc-9036-599b-a67a-fe185105b792",
    key="MCD17",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name",
    display_name="Crabrawler",
    searchable_by=["Crabrawler", "Basic", "Crabrawler"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="MCD17",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=739,
    abilities=[
        Attack(
            title="Punch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Crabhammer",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)