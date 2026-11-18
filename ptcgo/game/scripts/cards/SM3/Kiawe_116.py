from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.card_effects.trainers import basic_energy_of, ends_turn_after

card = SupporterCardDef(
    guid="be3ca5ba-43d8-5792-9d4c-6d4ea7da4d07",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kiawe.Name",
    display_name="Kiawe",
    searchable_by=["Kiawe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=116,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=ends_turn_after(search_attach_energy(basic_energy_of("fire"), count=4))
)
