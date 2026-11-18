from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import knocked_out_last_turn

card = SupporterCardDef(
    guid="357fcd88-9c1a-55d4-8a62-6c00a8960d33",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Diantha.Name",
    display_name="Diantha",
    searchable_by=["Diantha", "Supporter"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="SM6",
    rarity=Rarities.RareUltra,
    effect=recover_from_discard(None, count=2, to="hand"), condition=knocked_out_last_turn()
)
