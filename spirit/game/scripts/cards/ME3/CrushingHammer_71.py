from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_energy_opponent

card = ItemCardDef(
    guid="5cd3df1a-0018-55b2-b944-71c4607a97b3",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrushingHammer.Name",
    display_name="Crushing Hammer",
    searchable_by=["Crushing Hammer", "Item"],
    subtypes=["Item"],
    collector_number=71,
    set_code="ME3",
    rarity=Rarities.Common,
    effect=discard_energy_opponent(flip=True)
)
