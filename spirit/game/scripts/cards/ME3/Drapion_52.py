from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9391b3d0-ef32-5b9e-ac58-551bedc9032a",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drapion.Name",
    display_name="Drapion",
    searchable_by=["Drapion", "Stage 1", "Drapion"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name",
    family_id=451,
    abilities=[
        Attack(
            title="Wrack Down",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
        ),
        Attack(
            title="Hazardous Tail",
            game_text="This Pok\u00e9mon also does 70 damage to itself. Your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)