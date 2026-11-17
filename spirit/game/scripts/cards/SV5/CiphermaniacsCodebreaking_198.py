from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import search_to_top

card = SupporterCardDef(
    guid="6e63897a-0bd0-5e0a-99c9-ac237c1f44b0",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CiphermaniacsCodebreaking.Name",
    display_name="Ciphermaniac's Codebreaking",
    searchable_by=["Ciphermaniac's Codebreaking", "Supporter", "Future"],
    subtypes=["Supporter", "Future"],
    collector_number=198,
    set_code="SV5",
    rarity=Rarities.Rare,
    effect=search_to_top(2)
)
