from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import attach_discard_energy_to_each, has_subtype_in_play, is_basic_energy_card

card = ItemCardDef(
    guid="ae9a4fe3-90e0-5ada-9e7f-67e9aba3780b",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GlassTrumpet.Name",
    display_name="Glass Trumpet",
    searchable_by=["Glass Trumpet", "Item"],
    subtypes=["Item"],
    collector_number=135,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    effect=attach_discard_energy_to_each(is_basic_energy_card, per_target=1, targets=2), condition=has_subtype_in_play("Tera")
)
