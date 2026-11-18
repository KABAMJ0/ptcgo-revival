from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, CardType
from ptcgo.game.card_effects.support_common import search_to_hand


def _is_fairy_pokemon(card) -> bool:
    return (card.get_attribute(AttrID.CARD_TYPE) == CardType.POKEMON.value
            and PokemonTypes.FAIRY.value
            in (card.get_attribute(AttrID.POKEMON_TYPES) or []))

card = PokemonCardDef(
    guid="b4b5492e-5a85-596e-a73b-f59989cb4ea2",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name",
    display_name="Flabébé",
    searchable_by=["Flab\u00e9b\u00e9", "Basic", "Flabb"],
    subtypes=["Basic"],
    collector_number=149,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=669,
    abilities=[
        Attack(
            title="Floral Invitation",
            game_text="Search your deck for up to 2 Fairy Pok\u00e9mon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(_is_fairy_pokemon, count=2, reveal=True),
        ),
    ],
)