from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2ac32853-57c3-5cca-9639-dad2fd18a733",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miloticex.Name",
    display_name="Milotic ex",
    searchable_by=["Milotic ex", "Stage 1", "ex", "Miloticex"],
    subtypes=["Stage 1", "ex"],
    collector_number=96,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Ability(
            title="Mystic Scale",
            game_text="As long as Milotic ex is in play, each player can't play any Technical Machine cards from his or her hand. Discard all Technical Machine cards in play (both yours and your opponent's).",
            effect=unimplemented,
        ),
        Attack(
            title="Gentle Wrap",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Reflect Energy",
            game_text="Move 1 basic Energy card attached to Milotic ex to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=unimplemented,
        ),
    ],
)