from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import pokemon_of_subtype

card = ItemCardDef(
    guid="5ea73d73-f074-565b-b0ea-6e93160dca68",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeraOrb.Name",
    display_name="Tera Orb",
    searchable_by=["Tera Orb", "Item"],
    subtypes=["Item"],
    collector_number=189,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(pokemon_of_subtype("Tera"), count=1)
)
