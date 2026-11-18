from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_from_hand

card = ItemCardDef(
    guid="c5326647-dd87-5aa8-9bc6-ceb2cd9887ac",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=7,
    set_code="POP5",
    rarity=Rarities.Uncommon,
    effect=evolve_from_hand()
)
