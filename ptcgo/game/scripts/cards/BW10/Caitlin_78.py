from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_to_bottom_draw_per_card

card = SupporterCardDef(
    guid="0c2cf89d-b106-56ad-b7d6-aa9d046b34ae",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Caitlin.Name",
    display_name="Caitlin",
    searchable_by=["Caitlin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=78,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=hand_to_bottom_draw_per_card()
)
