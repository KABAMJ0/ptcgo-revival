from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities, TrainerType, PokemonTypes
from ptcgo.game.card_effects.passives_common import (attack_cost_modifier,
                                                     pokemon_of_types)
from ptcgo.game.card_effects.trainers import combine_passives
from ptcgo.game.session.passives import Passive


class PrismStarStadiumShield(Passive):
    """The clause both SM9 Prism Star Stadiums print: "Whenever any player
    plays an Item or Supporter card from their hand, prevent all effects of
    that card done to this Stadium card." The engine asks this hook while a
    Trainer effect names the Stadium itself (Effects.discard_stadium), and the
    printed wording shields it from its own owner as well as the opponent."""

    def blocks_trainer_effects(self, affected_player_id, trainer_card,
                               trainer_type, carrier, affected_entity=None,
                               board=None):
        if affected_entity is None \
                or affected_entity.entity_id != carrier.entity_id:
            return False
        return trainer_type in (TrainerType.ITEM.value,
                                TrainerType.SUPPORTER.value)


card = StadiumCardDef(
    guid="d51677c0-4efd-53b4-b1fb-50b59414cb3e",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WondrousLabyrinth.Name",
    display_name="Wondrous Labyrinth \u25c7",
    searchable_by=["Wondrous Labyrinth \u25c7", "Stadium", "Prism Star"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=158,
    set_code="SM9",
    rarity=Rarities.Rare,
    passive=combine_passives(
        attack_cost_modifier(
            1, pred=lambda p, b: not pokemon_of_types(PokemonTypes.FAIRY.value)(p)),
        PrismStarStadiumShield())
)
