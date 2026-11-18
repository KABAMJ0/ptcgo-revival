from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c337ba19-1bba-5c0c-971c-1373d839c0d1",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name",
    display_name="Steelix",
    searchable_by=["Steelix", "Stage 1", "Steelix"],
    subtypes=["Stage 1"],
    collector_number=104,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    family_id=95,
    abilities=[
        Attack(
            title="Ground Stream",
            game_text="Attach 2 Fighting Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Gigaton Shake",
            game_text="During your next turn, your Pok\u00e9mon can't attack. (This includes Pok\u00e9mon that come into play on that turn.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 4},
            damage=220,
            effect=unimplemented,
        ),
    ],
)