from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="630833a5-1dca-53b1-a95b-416eb8cabf9b",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquenex.Name",
    display_name="Vespiquen ex",
    searchable_by=["Vespiquen ex", "Stage 1", "ex", "Tera", "Vespiquenex"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=212,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    family_id=415,
    abilities=[
        Attack(
            title="Healing Pheromone",
            game_text="Heal 60 damage from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Phantom Queen",
            game_text="Put 3 damage counters on each of your opponent's Benched Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.GRASS: 3},
            damage=200,
            effect=unimplemented,
        ),
    ],
)