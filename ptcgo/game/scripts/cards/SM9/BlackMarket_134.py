from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities, TrainerType
from ptcgo.game.card_effects.trainers import fewer_prize_for_darkness_knockout
from ptcgo.game.session.passives import Passive


class BlackMarketPassive(Passive):
    """Two printed clauses: the opponent takes 1 fewer Prize card for a
    Darkness Pokemon with Darkness Energy knocked out by an attack (the
    factory passive), and no opposing Item or Supporter effect can touch this
    Stadium card."""

    def __init__(self):
        self._prizes = fewer_prize_for_darkness_knockout()

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        return self._prizes.modify_prizes_for_knockout(pokemon, ctx, count, carrier)

    def blocks_trainer_effects(self, affected_player_id, trainer_card,
                               trainer_type, carrier, affected_entity=None,
                               board=None):
        if affected_entity is None \
                or affected_entity.entity_id != carrier.entity_id:
            return False
        return trainer_type in (TrainerType.ITEM.value,
                                TrainerType.SUPPORTER.value)


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
    passive=BlackMarketPassive()
)
