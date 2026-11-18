from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_discard_to

card = ItemCardDef(
    guid="aae207ce-e0a0-5f25-8063-2e1c66e4d901",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HandTrimmer.Name",
    display_name="Hand Trimmer",
    searchable_by=["Hand Trimmer", "Item"],
    subtypes=["Item"],
    collector_number=150,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    effect=each_player_discard_to(5)
)
