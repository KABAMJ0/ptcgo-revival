from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_discard_to_hand

card = ItemCardDef(
    guid="9c5d0692-2693-5f40-8d83-cdc30271655c",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SurpriseBox.Name",
    display_name="Surprise Box",
    searchable_by=["Surprise Box", "Item"],
    subtypes=["Item"],
    collector_number=187,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=opponent_discard_to_hand(1)
)
