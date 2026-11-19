from ptcgo.game.data_utils import SupporterCardDef, is_pokemon_v
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand

card = SupporterCardDef(
    guid="90fa94f6-0135-5487-83a4-42ea9391db0c",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AdventurersDiscovery.Name",
    display_name="Adventurer's Discovery",
    searchable_by=["Adventurer's Discovery", "Supporter"],
    subtypes=["Supporter"],
    collector_number=23,
    set_code="SWSH11TG",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(
        lambda c: is_pokemon_v(c.archetype_id), count=3,
        prompt="Choose up to 3 Pokémon V",
    )
)
