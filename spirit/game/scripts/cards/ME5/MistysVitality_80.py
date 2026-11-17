from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import basic_energy_of, ends_turn_after

card = SupporterCardDef(
    guid="b03c5a33-0505-54d0-abbd-8d0286554575",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysVitality.Name",
    display_name="Misty's Vitality",
    searchable_by=["Misty's Vitality", "Supporter"],
    subtypes=["Supporter"],
    collector_number=80,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    effect=ends_turn_after(search_attach_energy(basic_energy_of("water"), count=4))
)
