from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_card, search_matching_opponent

card = ItemCardDef(
    guid="b465f9ba-d19f-5525-ae20-07558ae6934a",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LoveBall.Name",
    display_name="Love Ball",
    searchable_by=["Love Ball", "Item"],
    subtypes=["Item"],
    collector_number=156,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    effect=search_matching_opponent(is_pokemon_card, match="name", count=1)
)
