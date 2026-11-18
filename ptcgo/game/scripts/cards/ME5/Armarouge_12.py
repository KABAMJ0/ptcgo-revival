from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7ee0c2b4-413e-5fc8-9953-cb20f2beaf33",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armarouge.Name",
    display_name="Armarouge",
    searchable_by=["Armarouge", "Stage 1", "Armarouge"],
    subtypes=["Stage 1"],
    collector_number=12,
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