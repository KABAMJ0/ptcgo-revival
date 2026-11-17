from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import any_of, pokemon_type_subtype, with_discard_cost

card = ItemCardDef(
    guid="ec5d5ca1-5657-5a33-9f80-59e78075246c",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ElectromagneticRadar.Name",
    display_name="Electromagnetic Radar",
    searchable_by=["Electromagnetic Radar", "Item"],
    subtypes=["Item"],
    collector_number=169,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(2, search_to_hand(any_of(pokemon_type_subtype("lightning", "gx"), pokemon_type_subtype("lightning", "ex")), count=2))
)
