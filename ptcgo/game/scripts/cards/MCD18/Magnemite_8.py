from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="1ec03fa1-01a3-55b0-902f-b6eb4555001b",
    key="MCD18",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic", "Magnemite"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="MCD18",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=81,
    abilities=[
        Attack(
            title="Searching Magnet",
            game_text="Search your deck for up to 3 Metal Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(basic_energy_of("metal"), count=3, minimum=0, reveal=True),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
    ],
)