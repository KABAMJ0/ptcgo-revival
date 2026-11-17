from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import all_of, basic_energy_of, pokemon_of

card = SupporterCardDef(
    guid="e04662be-852b-55a9-9f4d-d88541116f8f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tulip.Name",
    display_name="Tulip",
    searchable_by=["Tulip", "Supporter"],
    subtypes=["Supporter"],
    collector_number=259,
    set_code="SV4",
    rarity=Rarities.Rare,
    effect=recover_from_discard(all_of(pokemon_of("psychic"), basic_energy_of("psychic")), count=4, to="hand")
)
