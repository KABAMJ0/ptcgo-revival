from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eb571baf-e5fe-5111-9d06-72ad24a66741",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigonex.Name",
    display_name="Hydreigon ex",
    searchable_by=["Hydreigon ex", "Stage 2", "Tera", "ex", "Hydreigonex"],
    subtypes=["Stage 2", "Tera", "ex"],
    collector_number=240,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Attack(
            title="Crashing Headbutt",
            game_text="Discard the top 3 cards of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
        Attack(
            title="Obsidian",
            game_text="This attack also does 130 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)