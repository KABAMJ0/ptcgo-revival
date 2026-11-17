from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card, opponent_prizes_in, pokemon_of_subtype

card = ItemCardDef(
    guid="202fb962-9248-5fc1-b227-36958fc09560",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeastRing.Name",
    display_name="Beast Ring",
    searchable_by=["Beast Ring", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="SM6",
    rarity=Rarities.Rare,
    effect=search_attach_energy(is_basic_energy_card, count=2, target_pred=pokemon_of_subtype("Ultra Beast"), distribute=False), condition=opponent_prizes_in(3, 4)
)
