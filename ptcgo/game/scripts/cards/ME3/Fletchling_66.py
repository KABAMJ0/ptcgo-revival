from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.session.effects import is_pokemon_card
from ptcgo.game.card_effects.support_common import search_to_hand


def _has_fighting_resistance(card):
    return (
        is_pokemon_card(card)
        and card.get_attribute(AttrID.RESISTANCE_TYPES) == PokemonTypes.FIGHTING.value
    )


card = PokemonCardDef(
    guid="1381b534-d13b-5557-b3b5-6a48b579018a",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name",
    display_name="Fletchling",
    searchable_by=["Fletchling", "Basic", "Fletchling"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="ME3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=661,
    abilities=[
        Attack(
            title="Chirp",
            game_text="Search your deck for up to 2 Pok\u00e9mon with Fighting Resistance, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(_has_fighting_resistance, count=2, minimum=0, reveal=True, prompt='Choose up to 2 Pokémon with Fighting Resistance.'),
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)