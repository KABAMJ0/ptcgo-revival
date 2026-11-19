from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.card_effects.trainers import (
    is_basic_energy_card, knocked_out_last_turn, pokemon_of,
)

card = SupporterCardDef(
    guid="107dfa23-b613-506d-86f4-3206fb13cb7a",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Zinnia.Name",
    display_name="Zinnia",
    searchable_by=["Zinnia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=70,
    set_code="DM",
    rarity=Rarities.RareUltra,
    effect=attach_from_hand(is_basic_energy_card, count=2, target="choice",
                            target_pred=pokemon_of("Dragon")),
    condition=knocked_out_last_turn()
)
