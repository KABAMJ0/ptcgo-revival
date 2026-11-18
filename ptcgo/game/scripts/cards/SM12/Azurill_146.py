from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.pokemon import is_energy_card
from ptcgo.game.card_effects.support_common import attach_from_discard


def _is_basic_energy(card) -> bool:
    return (is_energy_card(card)
            and not card.get_attribute(AttrID.IS_SPECIAL_ENERGY))


def _is_active(pokemon) -> bool:
    return is_in_active_spot(pokemon)

card = PokemonCardDef(
    guid="5586b2a5-e8ac-502b-b193-b28a28e055be",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azurill.Name",
    display_name="Azurill",
    searchable_by=["Azurill", "Basic", "Azurill"],
    subtypes=["Basic"],
    collector_number=146,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=298,
    abilities=[
        Ability(
            title="Growing Up",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, attach a basic Energy card from your discard pile to your Active Pok\u00e9mon. If you use this Ability, your turn ends.",
            effect=flip_gate(attach_from_discard(_is_basic_energy, count=1,
                                                target=_is_active)),
            ends_turn=True,
        ),
    ],
)