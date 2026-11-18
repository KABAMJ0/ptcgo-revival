from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_any, flip_recover_per_heads


_ELECTROCHARGER_RECOVERY = flip_recover_per_heads(2, card_named_any(["Electropower"]), to="deck_shuffle")


card = ItemCardDef(
    guid="39e9f59b-c13e-5f3c-ae47-dc6d8d834dd3",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Electrocharger.Name",
    display_name="Electrocharger",
    searchable_by=["Electrocharger", "Item"],
    subtypes=["Item"],
    collector_number=139,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=_ELECTROCHARGER_RECOVERY
)
