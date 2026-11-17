from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import attach_discard_energy_to_each, has_subtype_in_play, is_basic_energy_card

card = ItemCardDef(
    guid="fd98d661-f7d0-599b-adc9-bfb0f3a456e6",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GlassTrumpet.Name",
    display_name="Glass Trumpet",
    searchable_by=["Glass Trumpet", "Item"],
    subtypes=["Item"],
    collector_number=189,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    effect=attach_discard_energy_to_each(is_basic_energy_card, per_target=1, targets=2), condition=has_subtype_in_play("Tera")
)
