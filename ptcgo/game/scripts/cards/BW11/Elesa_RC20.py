from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_tool_card

card = SupporterCardDef(
    guid="15aac43c-a084-596e-b0ec-0c846f138b1d",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Elesa.Name",
    display_name="Elesa",
    searchable_by=["Elesa", "Supporter"],
    subtypes=["Supporter"],
    collector_number=1020,
    set_code="BW11",
    rarity=Rarities.Common,
    effect=search_to_hand(predicate=is_tool_card, count=3, minimum=3, prompt="Choose 3 Pokemon Tool cards")
)
