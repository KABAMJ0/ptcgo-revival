from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e4d2a989-55f1-5416-819a-257a4a8ab3c2",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frigibax.Name",
    display_name="Frigibax",
    searchable_by=["Frigibax", "Basic", "Frigibax"],
    subtypes=["Basic"],
    collector_number=208,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=996,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)