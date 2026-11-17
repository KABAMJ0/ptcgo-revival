from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import pokemon_of_subtype

card = ItemCardDef(
    guid="916b34e7-21fc-5874-b068-8a35ddffcda7",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegaSignal.Name",
    display_name="Mega Signal",
    searchable_by=["Mega Signal", "Item"],
    subtypes=["Item"],
    collector_number=193,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    effect=search_to_hand(pokemon_of_subtype("MEGA"), count=1)
)
