from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="175d39f3-5474-56ec-b0f4-9e0db3b36a4e",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudsdale.Name",
    display_name="Mudsdale",
    searchable_by=["Mudsdale", "Stage 1", "Mudsdale"],
    subtypes=["Stage 1"],
    collector_number=175,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name",
    family_id=749,
    abilities=[
        Attack(
            title="Mud Stock",
            game_text="Attach a Basic Fighting Energy card from your discard pile to each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="High Horsepower",
            game_text="This Pok\u00e9mon also does 40 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=unimplemented,
        ),
    ],
)