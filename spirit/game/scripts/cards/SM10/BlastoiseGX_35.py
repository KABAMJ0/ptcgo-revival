from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5fb9e5ca-b8b5-5c52-8245-ef02a064f574",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseGX.Name",
    display_name="Blastoise-GX",
    searchable_by=["Blastoise-GX", "Stage 2", "GX", "BlastoiseGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=35,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=240,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Solid Shell",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Rocket Splash",
            game_text="Shuffle any amount of Water Energy from your Pok\u00e9mon into your deck. This attack does 60 damage for each card you shuffled into your deck in this way.",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Giant Geyser-GX",
            game_text="Attach any number of Water Energy cards from your hand to your Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
    ],
)