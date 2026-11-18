from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_any, flip_recover_per_heads


_ELECTROCHARGER_RECOVERY = flip_recover_per_heads(2, card_named_any(["Electropower"]), to="deck_shuffle")


card = ItemCardDef(
    guid="78af3a11-93d0-541a-a3ac-5c7b59eda215",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Electrocharger.Name",
    display_name="Electrocharger",
    searchable_by=["Electrocharger", "Item"],
    subtypes=["Item"],
    collector_number=193,
    set_code="SM9",
    rarity=Rarities.RareSecret,
    effect=_ELECTROCHARGER_RECOVERY
)
