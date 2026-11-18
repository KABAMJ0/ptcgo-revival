from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import basic_energy_of

card = PokemonCardDef(
    guid="f0f3cabd-d9bc-586c-8ad9-bdff999b3f0a",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic", "Articuno"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="XY6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Attack(
            title="Find Ice",
            game_text="Search your deck for up to 3 Water Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_hand(basic_energy_of("water"), count=3, reveal=True),
        ),
        Attack(
            title="Freezing Wind",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)