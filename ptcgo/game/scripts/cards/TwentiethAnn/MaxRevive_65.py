from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_pokemon_card

card = ItemCardDef(
    guid="4ebc61ca-7af4-5584-b2af-df4d580918d5",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxRevive.Name",
    display_name="Max Revive",
    searchable_by=["Max Revive", "Item"],
    subtypes=["Item"],
    collector_number=65,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_pokemon_card, count=1, to="deck_top")
)
