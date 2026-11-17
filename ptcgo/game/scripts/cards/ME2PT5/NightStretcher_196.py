from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import any_of, is_basic_energy_card, is_pokemon_card

card = ItemCardDef(
    guid="8ce0ab7e-8373-5bb6-9a3f-d2b85138fb55",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightStretcher.Name",
    display_name="Night Stretcher",
    searchable_by=["Night Stretcher", "Item"],
    subtypes=["Item"],
    collector_number=196,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    effect=recover_from_discard(any_of(is_pokemon_card, is_basic_energy_card), count=1, to="hand")
)
