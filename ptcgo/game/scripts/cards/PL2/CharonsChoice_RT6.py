from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import rotom_identity_swap

card = SupporterCardDef(
    guid="4d8245da-5d38-5ab9-a6ee-2e55d1bc4c61",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CharonsChoice.Name",
    display_name="Charon's Choice",
    searchable_by=["Charon's Choice", "Supporter"],
    subtypes=["Supporter"],
    collector_number=6,
    set_code="PL2",
    rarity=Rarities.Rare,
    effect=rotom_identity_swap()
)
