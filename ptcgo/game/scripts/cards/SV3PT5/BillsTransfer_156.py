from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_pokemon_card

card = SupporterCardDef(
    guid="fd0a2e78-87ee-5940-a26b-e206cbe90d30",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsTransfer.Name",
    display_name="Bill's Transfer",
    searchable_by=["Bill's Transfer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=156,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    effect=look_at_top(8, take=1, predicate=is_pokemon_card)
)
