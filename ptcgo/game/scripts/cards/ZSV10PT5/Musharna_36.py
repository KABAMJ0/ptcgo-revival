from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import named

card = PokemonCardDef(
    guid="5723df2e-eb09-5a04-8d5d-6d13973a496e",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Musharna.Name",
    display_name="Musharna",
    searchable_by=["Musharna", "Stage 1", "Musharna"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="ZSV10PT5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    family_id=517,
    abilities=[
        Attack(
            title="Dream Calling",
            game_text="You may search your deck for any number of Fennel cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(named("fennel"), count=99, reveal=True),
        ),
        Attack(
            title="Sleep Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)