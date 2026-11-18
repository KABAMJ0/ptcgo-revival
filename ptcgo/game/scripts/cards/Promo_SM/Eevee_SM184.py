from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, CardType
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.support_common import search_to_hand


def _is_pokemon(card) -> bool:
    return card.get_attribute(AttrID.CARD_TYPE) == CardType.POKEMON.value

card = PokemonCardDef(
    guid="afa65e00-b4ee-5481-a434-81042ab503fd",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=184,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text="Flip a coin. If heads, search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_gate(search_to_hand(_is_pokemon, count=1, reveal=True)),
        ),
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)