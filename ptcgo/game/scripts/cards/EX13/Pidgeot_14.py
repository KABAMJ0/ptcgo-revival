from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="84fb6292-fb3f-5132-b7c5-62e85ea4985c",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name",
    display_name="Pidgeot δ",
    searchable_by=["Pidgeot \u03b4", "Stage 2", "Pidgeot"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    family_id=18,
    abilities=[
        Ability(
            title="Delta Reserve",
            game_text="As long as Pidgeot has any Holon Energy cards attached to it, each player's Pok\u00e9mon (excluding Pok\u00e9mon that has \u03b4 on its card) can't use any Pok\u00e9-Powers.",
            effect=unimplemented,
        ),
        Attack(
            title="Rotating Claws",
            game_text="You may discard an Energy card attached to Pidgeot. If you do, search your discard pile for an Energy card (excluding the one you discarded) and attach it to Pidgeot.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)