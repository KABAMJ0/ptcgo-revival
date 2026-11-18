from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, card_named_contains, choose_one
from ptcgo.game.session.effects import is_supporter_card
from ptcgo.game.card_effects.support_common import recover_from_discard, search_to_hand

_HOLON_SUPPORTER = all_of(is_supporter_card, card_named_contains("Holon"))


_HOLON_TRANSCEIVER = choose_one([
    ("Search your deck", search_to_hand(_HOLON_SUPPORTER, 1)),
    ("Search your discard pile",
     recover_from_discard(_HOLON_SUPPORTER, 1, minimum=0, reveal=True)),
])


card = ItemCardDef(
    guid="04caf74a-9cd8-5f0e-804e-cea91f974739",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonTransceiver.Name",
    display_name="Holon Transceiver",
    searchable_by=["Holon Transceiver", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    effect=_HOLON_TRANSCEIVER
)
