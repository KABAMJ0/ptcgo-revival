from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of, switch_then_heal

card = ItemCardDef(
    guid="2ed35178-8ed0-5430-a25a-0248454daed4",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SwitchRaft.Name",
    display_name="Switch Raft",
    searchable_by=["Switch Raft", "Item"],
    subtypes=["Item"],
    collector_number=77,
    set_code="DM",
    rarity=Rarities.RareSecret,
    effect=switch_then_heal(30, active_pred=pokemon_of("Water"))
)
