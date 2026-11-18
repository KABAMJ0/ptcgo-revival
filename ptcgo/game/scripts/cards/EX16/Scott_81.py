from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, is_stadium_card
from ptcgo.game.session.effects import is_supporter_card
from ptcgo.game.card_effects.support_common import search_to_hand

card = SupporterCardDef(
    guid="8a04dc42-a913-55c4-81d3-a7a3d486c6d0",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Scott.Name",
    display_name="Scott",
    searchable_by=["Scott", "Supporter"],
    subtypes=["Supporter"],
    collector_number=81,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(any_of(is_supporter_card, is_stadium_card), 3)
)
