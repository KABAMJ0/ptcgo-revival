from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import knocked_out_last_turn, pokemon_of

card = SupporterCardDef(
    guid="e3ebff2a-f53c-550d-afcf-caf8d079d6ab",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lance.Name",
    display_name="Lance ◇",
    searchable_by=["Lance \u25c7", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=61,
    set_code="DM",
    rarity=Rarities.Rare,
    effect=search_to_bench(pokemon_of("Dragon"), count=2),
    condition=knocked_out_last_turn()
)
