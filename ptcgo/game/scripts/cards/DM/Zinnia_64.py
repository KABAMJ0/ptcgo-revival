from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card, knocked_out_last_turn, pokemon_of

card = SupporterCardDef(
    guid="1fc05985-a25a-5825-a3eb-e83c8ae36363",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Zinnia.Name",
    display_name="Zinnia",
    searchable_by=["Zinnia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=64,
    set_code="DM",
    rarity=Rarities.Uncommon,
    effect=attach_from_hand(is_basic_energy_card, count=2, target="choice", target_pred=pokemon_of("Dragon")),
    condition=knocked_out_last_turn()
)
