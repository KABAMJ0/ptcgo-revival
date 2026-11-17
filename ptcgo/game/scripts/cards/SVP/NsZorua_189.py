from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="795946b5-3253-5121-8bad-8d9266ce28be",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsZorua.Name",
    display_name="N's Zorua",
    searchable_by=["N's Zorua", "Basic", "NsZorua"],
    subtypes=["Basic"],
    collector_number=189,
    set_code="SVP",
    rarity=Rarities.RarePromo,
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