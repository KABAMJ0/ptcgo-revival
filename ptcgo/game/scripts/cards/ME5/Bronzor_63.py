from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="63d4f044-8a38-5353-a80b-2501eec114c2",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    display_name="Bronzor",
    searchable_by=["Bronzor", "Basic", "Bronzor"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=436,
    abilities=[
        Attack(
            title="Mirror Attack",
            game_text="If your opponent's Active Pok\u00e9mon is a Metal Pok\u00e9mon, this attack does 30 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)