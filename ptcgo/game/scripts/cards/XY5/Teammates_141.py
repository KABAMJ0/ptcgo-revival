from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import knocked_out_last_turn

card = SupporterCardDef(
    guid="846718aa-ccef-5fe9-9a33-647af4f4e0dc",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Teammates.Name",
    display_name="Teammates",
    searchable_by=["Teammates", "Supporter"],
    subtypes=["Supporter"],
    collector_number=141,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(None, count=2), condition=knocked_out_last_turn()
)
