from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import pokemon_of_subtype

card = ItemCardDef(
    guid="fa70ef3e-1626-5313-8467-278e0072161a",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegaSignal.Name",
    display_name="Mega Signal",
    searchable_by=["Mega Signal", "Item"],
    subtypes=["Item"],
    collector_number=121,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(pokemon_of_subtype("MEGA"), count=1)
)
