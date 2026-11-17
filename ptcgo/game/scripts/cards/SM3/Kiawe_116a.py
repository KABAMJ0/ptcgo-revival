from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.card_effects.trainers import basic_energy_of, ends_turn_after

card = SupporterCardDef(
    guid="130e957e-5c0a-5723-a7b3-98f01e283537",
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
