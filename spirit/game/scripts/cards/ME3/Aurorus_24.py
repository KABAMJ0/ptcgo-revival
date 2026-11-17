from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d41c7e50-9891-5283-bc56-44df2d807308",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aurorus.Name",
    display_name="Aurorus",
    searchable_by=["Aurorus", "Stage 2", "Aurorus"],
    subtypes=["Stage 2"],
    collector_number=24,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Amaura.Name",
    family_id=698,
    abilities=[
        Ability(
            title="Tundra Wall",
            game_text="All of your Pok\u00e9mon that have any Water Energy attached take 50 less damage from attacks from your opponent's Pok\u00e9mon (after applying Weakness and Resistance). The effect of Tundra Wall doesn't stack.",
            effect=unimplemented,
        ),
        Attack(
            title="Freezing Chill",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't use attacks.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)