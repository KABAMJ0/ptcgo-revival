from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import named_one_of
from ptcgo.game.card_effects.support_common import recover_from_discard

card = ItemCardDef(
    guid="0348e1db-4ecb-513f-a4a5-d205e26ab877",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilExcavationKit.Name",
    display_name="Fossil Excavation Kit",
    searchable_by=["Fossil Excavation Kit", "Item"],
    subtypes=["Item"],
    collector_number=101,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(
        named_one_of("Helix Fossil Omanyte", "Dome Fossil Kabuto",
                     "Old Amber Aerodactyl", "Helix Fossil", "Dome Fossil",
                     "Old Amber"),
        2, reveal=True),
)
