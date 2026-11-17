from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_energy_opponent

card = ItemCardDef(
    guid="b4de586b-4dbf-5e31-9769-5b02ee5f6266",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrushingHammer.Name",
    display_name="Crushing Hammer",
    searchable_by=["Crushing Hammer", "Item"],
    subtypes=["Item"],
    collector_number=105,
    set_code="ME5",
    rarity=Rarities.Rare,
    effect=discard_energy_opponent(flip=True)
)
