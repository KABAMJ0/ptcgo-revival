from ptcgo.game.card_effects.passives_common import (
    item_or_supporter_effect_shield,
)
from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (combine_passives,
                                              fewer_prize_for_darkness_knockout)


card = StadiumCardDef(
    guid="8713634e-a490-56c7-b72f-a119019d7101",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlackMarket.Name",
    display_name="Black Market \u25c7",
    searchable_by=["Black Market \u25c7", "Stadium", "Prism Star"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=134,
    set_code="SM9",
    rarity=Rarities.Rare,
    passive=combine_passives(fewer_prize_for_darkness_knockout(),
                             item_or_supporter_effect_shield(
        protects=lambda entity, carrier: entity is not None
        and entity.entity_id == carrier.entity_id, any_player=True))
)
