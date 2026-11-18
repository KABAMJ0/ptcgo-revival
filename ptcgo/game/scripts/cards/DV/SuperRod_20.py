from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, is_pokemon_card, shuffle_discard_combo_into_deck

card = ItemCardDef(
    guid="fc5a47d9-5dfb-5eaa-8c89-eca0cfd3c316",
    key="DV",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperRod.Name",
    display_name="Super Rod",
    searchable_by=["Super Rod", "Item"],
    subtypes=["Item"],
    collector_number=20,
    set_code="DV",
    rarity=Rarities.RareHolo,
    effect=shuffle_discard_combo_into_deck(3, is_pokemon_card, is_basic_energy_card)
)
