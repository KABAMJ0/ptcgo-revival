from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_and_discard

card = ItemCardDef(
    guid="2af80aaa-b14a-5472-8a4f-6906f780a5a7",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleCompressorTeamFlareGear.Name",
    display_name="Battle Compressor Team Flare Gear",
    searchable_by=["Battle Compressor Team Flare Gear", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    effect=search_and_discard(3)
)
