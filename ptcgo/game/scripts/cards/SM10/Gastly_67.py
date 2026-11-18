from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import named

card = PokemonCardDef(
    guid="b850b6dc-c7ae-5d88-81b4-9ecd394541f2",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic", "Gastly"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Ability(
            title="Swelling Spite",
            game_text="When this Pok\u00e9mon is Knocked Out, search your deck for up to 2 Haunter and put them onto your Bench. Then, shuffle your deck.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=search_to_bench(named("haunter"), count=2),
        ),
        Attack(
            title="Will-O-Wisp",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)