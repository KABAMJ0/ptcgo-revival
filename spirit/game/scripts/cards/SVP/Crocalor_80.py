from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="20d83a45-1439-5d67-b558-d5616126b5f9",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name",
    display_name="Crocalor",
    searchable_by=["Crocalor", "Stage 1", "Crocalor"],
    subtypes=["Stage 1"],
    collector_number=80,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name",
    family_id=909,
    abilities=[
        Attack(
            title="Steady Firebreathing",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.FIRE: 2},
            damage=70,
        ),
    ],
)