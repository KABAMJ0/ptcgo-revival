from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import all_of, basic_energy_of, pokemon_of

card = SupporterCardDef(
    guid="aeb561b6-8d1f-5d13-b887-ae0ee4c0bccc",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tulip.Name",
    display_name="Tulip",
    searchable_by=["Tulip", "Supporter"],
    subtypes=["Supporter"],
    collector_number=181,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(all_of(pokemon_of("psychic"), basic_energy_of("psychic")), count=4, to="hand")
)
