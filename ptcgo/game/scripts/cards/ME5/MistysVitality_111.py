from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.card_effects.trainers import basic_energy_of, ends_turn_after

card = SupporterCardDef(
    guid="269a2a13-b823-50ef-8e0f-6b8583ce9cfc",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysVitality.Name",
    display_name="Misty's Vitality",
    searchable_by=["Misty's Vitality", "Supporter"],
    subtypes=["Supporter"],
    collector_number=111,
    set_code="ME5",
    rarity=Rarities.Rare,
    effect=ends_turn_after(search_attach_energy(basic_energy_of("water"), count=4))
)
