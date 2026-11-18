from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_to_bottom_draw

card = SupporterCardDef(
    guid="dbdae281-8841-5859-9c77-82b5b87ac662",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kofu.Name",
    display_name="Kofu",
    searchable_by=["Kofu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=138,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    effect=hand_to_bottom_draw(2, 4)
)
