from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_two_kinds_to_bench

card = SupporterCardDef(
    guid="562e45e6-0f03-5a12-b9b3-9be90088ecb3",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brigette.Name",
    display_name="Brigette",
    searchable_by=["Brigette", "Supporter"],
    subtypes=["Supporter"],
    collector_number=134,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=search_two_kinds_to_bench(1, 3)
)
