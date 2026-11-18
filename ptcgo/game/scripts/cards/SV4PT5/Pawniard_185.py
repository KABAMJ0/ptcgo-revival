from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="870ccd52-1cd0-5a93-a575-139c8dd134e3",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    display_name="Pawniard",
    searchable_by=["Pawniard", "Basic", "Pawniard"],
    subtypes=["Basic"],
    collector_number=185,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=624,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)