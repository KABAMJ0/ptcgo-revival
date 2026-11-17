from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_energy_each_opponent, is_special_energy

card = SupporterCardDef(
    guid="8ebc506b-1b1c-5487-a760-fdecc3ec3f2a",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Giacomo.Name",
    display_name="Giacomo",
    searchable_by=["Giacomo", "Supporter"],
    subtypes=["Supporter"],
    collector_number=182,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    effect=discard_energy_each_opponent(predicate=is_special_energy)
)
