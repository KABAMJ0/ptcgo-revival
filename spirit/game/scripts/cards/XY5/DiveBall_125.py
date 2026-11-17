from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import pokemon_of

card = ItemCardDef(
    guid="ff945cff-af8d-5a5a-af6e-ba30662bf1fe",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DiveBall.Name",
    display_name="Dive Ball",
    searchable_by=["Dive Ball", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(pokemon_of("water"), count=1)
)
