from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="981ee80a-4733-5f44-8c30-95460e9d2ec7",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name",
    display_name="Cascoon",
    searchable_by=["Cascoon", "Stage 1", "Cascoon"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Trading Places",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
    ],
)