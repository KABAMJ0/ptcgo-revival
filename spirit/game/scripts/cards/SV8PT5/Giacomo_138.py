from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_energy_each_opponent, is_special_energy

card = SupporterCardDef(
    guid="61477dc1-1c94-5836-b0ee-f61148a0fd9d",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Giacomo.Name",
    display_name="Giacomo",
    searchable_by=["Giacomo", "Supporter"],
    subtypes=["Supporter"],
    collector_number=138,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=discard_energy_each_opponent(predicate=is_special_energy)
)
