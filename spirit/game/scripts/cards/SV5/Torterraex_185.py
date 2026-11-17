from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5dada387-1990-5b74-89f4-ee7be1e1da35",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torterraex.Name",
    display_name="Torterra ex",
    searchable_by=["Torterra ex", "Stage 2", "ex", "Torterraex"],
    subtypes=["Stage 2", "ex"],
    collector_number=185,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name",
    family_id=387,
    abilities=[
        Attack(
            title="Forest March",
            game_text="This attack does 30 damage for each of your Grass Pok\u00e9mon in play.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Jungle Hammer",
            game_text="Heal 50 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=unimplemented,
        ),
    ],
)