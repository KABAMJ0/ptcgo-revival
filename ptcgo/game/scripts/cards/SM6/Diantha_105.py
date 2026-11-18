from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import knocked_out_last_turn

card = SupporterCardDef(
    guid="3cc15279-2c3e-50aa-960c-1fc236e33ca7",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Diantha.Name",
    display_name="Diantha",
    searchable_by=["Diantha", "Supporter"],
    subtypes=["Supporter"],
    collector_number=105,
    set_code="SM6",
    rarity=Rarities.RareHolo,
    effect=recover_from_discard(None, count=2, to="hand"), condition=knocked_out_last_turn()
)
