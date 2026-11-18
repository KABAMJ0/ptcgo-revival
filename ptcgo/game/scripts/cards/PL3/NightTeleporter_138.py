from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_to_top_then_any_search

card = ItemCardDef(
    guid="aa9bd243-2fb7-5e6c-9eca-be3ff1c35ba3",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightTeleporter.Name",
    display_name="Night Teleporter",
    searchable_by=["Night Teleporter", "Item"],
    subtypes=["Item"],
    collector_number=138,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    effect=hand_to_top_then_any_search(1)
)
