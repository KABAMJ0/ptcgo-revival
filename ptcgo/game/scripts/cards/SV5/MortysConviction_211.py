from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_per_opponent_bench, with_discard_cost

card = SupporterCardDef(
    guid="8402f5b6-8123-5551-9372-9ba0f5406389",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MortysConviction.Name",
    display_name="Morty's Conviction",
    searchable_by=["Morty's Conviction", "Supporter"],
    subtypes=["Supporter"],
    collector_number=211,
    set_code="SV5",
    rarity=Rarities.Rare,
    effect=with_discard_cost(1, draw_per_opponent_bench(1))
)
