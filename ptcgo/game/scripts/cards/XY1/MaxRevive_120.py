from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_pokemon_card

card = ItemCardDef(
    guid="bdfab0b2-e405-5f82-9a79-2dcf3987e2ed",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxRevive.Name",
    display_name="Max Revive",
    searchable_by=["Max Revive", "Item"],
    subtypes=["Item"],
    collector_number=120,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_pokemon_card, count=1, to="deck_top")
)
