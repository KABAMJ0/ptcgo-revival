from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_energy_opponent

card = ItemCardDef(
    guid="8ab98fef-79fd-5d16-87c0-56abb0195281",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrushingHammer.Name",
    display_name="Crushing Hammer",
    searchable_by=["Crushing Hammer", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    effect=discard_energy_opponent(flip=True)
)
