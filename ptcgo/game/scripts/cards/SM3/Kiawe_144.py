from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.card_effects.trainers import basic_energy_of, ends_turn_after

card = SupporterCardDef(
    guid="760aaaff-5595-5285-9b77-e4236bdfaf99",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kiawe.Name",
    display_name="Kiawe",
    searchable_by=["Kiawe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=144,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    effect=ends_turn_after(search_attach_energy(basic_energy_of("fire"), count=4))
)
