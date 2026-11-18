from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_per_opponent_bench, with_discard_cost

card = SupporterCardDef(
    guid="9f55be13-4a52-5bc0-a353-a12a6929ec34",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MortysConviction.Name",
    display_name="Morty's Conviction",
    searchable_by=["Morty's Conviction", "Supporter"],
    subtypes=["Supporter"],
    collector_number=155,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, draw_per_opponent_bench(1))
)
