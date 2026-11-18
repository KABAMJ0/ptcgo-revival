from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of

card = ItemCardDef(
    guid="3e059737-81d7-5c70-89fb-9acba4c54819",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FireCrystal.Name",
    display_name="Fire Crystal",
    searchable_by=["Fire Crystal", "Item"],
    subtypes=["Item"],
    collector_number=231,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    effect=recover_from_discard(basic_energy_of("fire"), count=3, to="hand")
)
