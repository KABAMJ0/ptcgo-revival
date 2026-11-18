from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_from_hand

card = ItemCardDef(
    guid="a1fc4a8b-8c18-56fa-a213-8524cd7ec8ec",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=135,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=evolve_from_hand()
)
