from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import pokemon_of

card = ItemCardDef(
    guid="973254e4-58c2-502b-96d2-2ce49008a4bb",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Revitalizer.Name",
    display_name="Revitalizer",
    searchable_by=["Revitalizer", "Item"],
    subtypes=["Item"],
    collector_number=70,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(pokemon_of("grass"), count=2, to="hand")
)
