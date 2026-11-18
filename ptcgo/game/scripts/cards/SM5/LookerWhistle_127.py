from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import card_named_contains

card = ItemCardDef(
    guid="be2917bb-9f22-5f45-9c31-37495b84cc06",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LookerWhistle.Name",
    display_name="Looker Whistle",
    searchable_by=["Looker Whistle", "Item"],
    subtypes=["Item"],
    collector_number=127,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(card_named_contains("looker"), count=2)
)
