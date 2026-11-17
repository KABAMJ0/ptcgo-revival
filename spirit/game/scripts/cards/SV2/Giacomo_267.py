from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_energy_each_opponent, is_special_energy

card = SupporterCardDef(
    guid="aa39d9da-ee04-514d-9998-75af4315ca4d",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Giacomo.Name",
    display_name="Giacomo",
    searchable_by=["Giacomo", "Supporter"],
    subtypes=["Supporter"],
    collector_number=267,
    set_code="SV2",
    rarity=Rarities.Rare,
    effect=discard_energy_each_opponent(predicate=is_special_energy)
)
