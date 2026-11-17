from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4da95940-e771-5d48-b8ae-91f3800ce9c1",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    display_name="Spewpa",
    searchable_by=["Spewpa", "Stage 1", "Spewpa"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name",
    family_id=664,
    abilities=[
        Attack(
            title="Wander About",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)