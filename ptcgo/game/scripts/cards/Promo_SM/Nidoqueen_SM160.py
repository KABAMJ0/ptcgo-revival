from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, CardType
from ptcgo.game.card_effects.attacks_common import count_bench, damage_per
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.data_utils import subtypes_for


def _is_plain_pokemon(card) -> bool:
    if card.get_attribute(AttrID.CARD_TYPE) != CardType.POKEMON.value:
        return False
    subtypes = subtypes_for(card.archetype_id)
    return "GX" not in subtypes and "EX" not in subtypes


def _is_evolved(pokemon) -> bool:
    return any(subtype in ("Stage 1", "Stage 2", "VMAX", "BREAK")
               for subtype in subtypes_for(pokemon.archetype_id))

card = PokemonCardDef(
    guid="5f7be99b-82cc-5f97-9aae-598ed16d6830",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name",
    display_name="Nidoqueen",
    searchable_by=["Nidoqueen", "Stage 2", "Nidoqueen"],
    subtypes=["Stage 2"],
    collector_number=160,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    family_id=31,
    abilities=[
        Ability(
            title="Queen's Call",
            game_text="Once during your turn (before your attack), you may search your deck for a Pok\u00e9mon that isn't a Pok\u00e9mon-GX or Pok\u00e9mon-EX, reveal it, and put it into your hand. Then, shuffle your deck.",
            effect=search_to_hand(_is_plain_pokemon, count=1, reveal=True),
        ),
        Attack(
            title="Power Lariat",
            game_text="This attack does 50 more damage for each Evolution Pok\u00e9mon on your Bench.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_bench("mine", _is_evolved), 50, base=10),
        ),
    ],
)