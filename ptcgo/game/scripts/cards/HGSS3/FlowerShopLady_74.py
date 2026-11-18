from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import recover_two_kinds_to_deck

card = SupporterCardDef(
    guid="ccfc1d5e-66ee-5ce6-a99f-cee383d90773",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FlowerShopLady.Name",
    display_name="Flower Shop Lady",
    searchable_by=["Flower Shop Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=74,
    set_code="HGSS3",
    rarity=Rarities.Uncommon,
    effect=recover_two_kinds_to_deck(3, 3)
)
