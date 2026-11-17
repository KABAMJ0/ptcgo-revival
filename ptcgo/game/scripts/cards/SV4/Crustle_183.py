from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="68010426-ff93-5166-96cf-9ad61638ecb5",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crustle.Name",
    display_name="Crustle",
    searchable_by=["Crustle", "Stage 1", "Crustle"],
    subtypes=["Stage 1"],
    collector_number=183,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name",
    family_id=557,
    abilities=[
        Attack(
            title="Confront",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Crag Bash",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 100 less damage from attacks from Evolution Pok\u00e9mon (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)