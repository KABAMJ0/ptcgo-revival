from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="abff9c36-be6c-577b-ac82-8d34e291888a",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja", "Stage 1", "Shedinja"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Empty Shell",
            game_text="When Shedinja is Knocked Out, your opponent doesn't take any Prize cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Extra Curse",
            game_text="Put 2 damage counters on the Defending Pok\u00e9mon. If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, put 4 damage counters instead.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)