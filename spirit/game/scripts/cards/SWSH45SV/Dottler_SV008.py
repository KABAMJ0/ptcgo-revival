from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4340e37e-a7d7-59ca-b137-8d6bcca8fd08",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dottler.Name",
    display_name="Dottler",
    searchable_by=["Dottler", "Stage 1", "Dottler"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Blipbug.Name",
    family_id=824,
    abilities=[
        Attack(
            title="Reflect",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 40 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)