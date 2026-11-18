from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_pokemon_card

card = SupporterCardDef(
    guid="dd77291d-29b8-5cae-9ab9-81603abb5537",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsTransfer.Name",
    display_name="Bill's Transfer",
    searchable_by=["Bill's Transfer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=194,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    effect=look_at_top(8, take=8, predicate=is_pokemon_card, minimum=0)
)
