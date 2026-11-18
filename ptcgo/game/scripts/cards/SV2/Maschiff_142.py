from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dfd73516-ad65-58e6-8248-80ab33b50026",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name",
    display_name="Maschiff",
    searchable_by=["Maschiff", "Basic", "Maschiff"],
    subtypes=["Basic"],
    collector_number=142,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=942,
    abilities=[
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)