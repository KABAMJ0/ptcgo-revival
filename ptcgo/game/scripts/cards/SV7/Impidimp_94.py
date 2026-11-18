from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3587414d-d8e5-5032-993e-31e2a4da04ad",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Impidimp.Name",
    display_name="Impidimp",
    searchable_by=["Impidimp", "Basic", "Impidimp"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=859,
    abilities=[
        Attack(
            title="Smack",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)