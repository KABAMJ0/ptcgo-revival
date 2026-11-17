from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_energy_opponent

card = ItemCardDef(
    guid="84d8563f-3b58-5072-a5f0-bab559af231c",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrushingHammer.Name",
    display_name="Crushing Hammer",
    searchable_by=["Crushing Hammer", "Item"],
    subtypes=["Item"],
    collector_number=115,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=discard_energy_opponent(flip=True)
)
