from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, card_named_contains, is_evolution_pokemon

card = ItemCardDef(
    guid="7edfb317-233e-5d9e-8d12-b4377eef480b",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TheBosssWay.Name",
    display_name="The Boss's Way",
    searchable_by=["The Boss's Way"],
    subtypes=[],
    collector_number=105,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_evolution_pokemon, card_named_contains("dark")), count=1)
)
