from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_energy_opponent

card = ItemCardDef(
    guid="adb6d1e9-6299-5b7f-9858-1741ca85655d",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrushingHammer.Name",
    display_name="Crushing Hammer",
    searchable_by=["Crushing Hammer", "Item"],
    subtypes=["Item"],
    collector_number=166,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    effect=discard_energy_opponent(flip=True)
)
