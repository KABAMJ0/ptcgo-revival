from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.card_effects.passives_common import energy_return_on_discard_passive
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="49d16f73-cbb4-58d7-ad36-fc862a7a73be",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ecogym.Name",
    display_name="Ecogym",
    searchable_by=["Ecogym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=84,
    set_code="NEO1",
    rarity=Rarities.Rare,
    passive=energy_return_on_discard_passive()
)
