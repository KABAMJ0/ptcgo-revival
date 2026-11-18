from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, is_pokemon_card, shuffle_discard_combo_into_deck

card = ItemCardDef(
    guid="d45fb5ac-30e9-5b8b-b498-be0690ffa856",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperRod.Name",
    display_name="Super Rod",
    searchable_by=["Super Rod", "Item"],
    subtypes=["Item"],
    collector_number=95,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    effect=shuffle_discard_combo_into_deck(3, is_pokemon_card, is_basic_energy_card)
)
