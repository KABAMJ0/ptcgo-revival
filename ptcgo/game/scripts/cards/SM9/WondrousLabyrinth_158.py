from ptcgo.game.card_effects.passives_common import (
    item_or_supporter_effect_shield,
)
from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities, PokemonTypes
from ptcgo.game.card_effects.passives_common import (attack_cost_modifier,
                                                     pokemon_of_types)
from ptcgo.game.card_effects.trainers import combine_passives


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
        item_or_supporter_effect_shield(
        protects=lambda entity, carrier: entity is not None
        and entity.entity_id == carrier.entity_id, any_player=True))
)
