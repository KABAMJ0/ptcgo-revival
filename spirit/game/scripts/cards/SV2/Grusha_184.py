from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_until_unless_energy

card = SupporterCardDef(
    guid="73a1519e-35c6-58e7-aec5-7afb86491ea0",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Grusha.Name",
    display_name="Grusha",
    searchable_by=["Grusha", "Supporter"],
    subtypes=["Supporter"],
    collector_number=184,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    effect=draw_until_unless_energy(5, 7)
)
