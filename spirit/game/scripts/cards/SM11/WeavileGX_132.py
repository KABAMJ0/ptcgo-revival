from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="95d0a59a-9cb3-5032-beeb-a405170a7ca6",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WeavileGX.Name",
    display_name="Weavile-GX",
    searchable_by=["Weavile-GX", "Stage 1", "GX", "WeavileGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=132,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=200,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Ability(
            title="Shadow Connection",
            game_text="As often as you like during your turn (before your attack), you may move a basic Darkness Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title="Nocturnal Maneuvers-GX",
            game_text="Search your deck for any number of Basic Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)