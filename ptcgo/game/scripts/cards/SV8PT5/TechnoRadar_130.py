from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import pokemon_of_subtype, with_discard_cost

card = ItemCardDef(
    guid="53189343-e9df-5abb-a357-72830da5532b",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnoRadar.Name",
    display_name="Techno Radar",
    searchable_by=["Techno Radar", "Item", "Future"],
    subtypes=["Item", "Future"],
    collector_number=130,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, search_to_hand(pokemon_of_subtype("Future"), count=2))
)
