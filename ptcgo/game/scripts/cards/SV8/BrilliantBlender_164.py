from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_and_discard

card = ItemCardDef(
    guid="aec550bb-f88c-50df-b674-3706730046cf",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrilliantBlender.Name",
    display_name="Brilliant Blender",
    searchable_by=["Brilliant Blender", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=164,
    set_code="SV8",
    rarity=Rarities.Rare,
    effect=search_and_discard(5)
)
