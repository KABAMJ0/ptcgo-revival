from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="29ce524d-9d44-5bbb-9afa-89f3373888f4",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armarouge.Name",
    display_name="Armarouge",
    searchable_by=["Armarouge", "Stage 1", "Armarouge"],
    subtypes=["Stage 1"],
    collector_number=86,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Attack(
            title="Flame Legion",
            game_text="This attack does 40 more damage for each of your Benched Pok\u00e9mon that has any Fire Energy attached.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)