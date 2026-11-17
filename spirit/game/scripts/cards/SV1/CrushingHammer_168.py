from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_energy_opponent

card = ItemCardDef(
    guid="9ad1ecab-58b6-59b8-b6e9-fc6ac716def3",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrushingHammer.Name",
    display_name="Crushing Hammer",
    searchable_by=["Crushing Hammer", "Item"],
    subtypes=["Item"],
    collector_number=168,
    set_code="SV1",
    rarity=Rarities.Common,
    effect=discard_energy_opponent(flip=True)
)
