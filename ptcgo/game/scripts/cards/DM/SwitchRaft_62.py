from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of, switch_then_heal

card = ItemCardDef(
    guid="09cc0b2d-be04-5aa3-804c-e300eb45ab0c",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SwitchRaft.Name",
    display_name="Switch Raft",
    searchable_by=["Switch Raft", "Item"],
    subtypes=["Item"],
    collector_number=62,
    set_code="DM",
    rarity=Rarities.Uncommon,
    effect=switch_then_heal(30, active_pred=pokemon_of("Water"))
)
