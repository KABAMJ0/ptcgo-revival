from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="75bf6e23-4b96-5217-ab7b-a0c7d515b131",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsZorua.Name",
    display_name="N's Zorua",
    searchable_by=["N's Zorua", "Basic", "NsZorua"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=570,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)