from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_energy_opponent

card = ItemCardDef(
    guid="b0292efc-b546-59bd-bebe-1c5e813452f4",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrushingHammer.Name",
    display_name="Crushing Hammer",
    searchable_by=["Crushing Hammer", "Item"],
    subtypes=["Item"],
    collector_number=60,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=discard_energy_opponent(flip=True)
)
