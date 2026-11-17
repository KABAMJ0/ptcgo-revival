from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_draw

card = SupporterCardDef(
    guid="9e454373-0ca6-5331-a74e-5efac6f13590",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Youngster.Name",
    display_name="Youngster",
    searchable_by=["Youngster", "Supporter"],
    subtypes=["Supporter"],
    collector_number=198,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw(5)
)
