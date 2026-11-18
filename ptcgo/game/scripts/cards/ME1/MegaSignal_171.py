from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import pokemon_of_subtype

card = ItemCardDef(
    guid="aa17d6e6-95ff-54af-9fc8-da00059c8d62",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegaSignal.Name",
    display_name="Mega Signal",
    searchable_by=["Mega Signal", "Item"],
    subtypes=["Item"],
    collector_number=171,
    set_code="ME1",
    rarity=Rarities.Rare,
    effect=search_to_hand(pokemon_of_subtype("MEGA"), count=1)
)
