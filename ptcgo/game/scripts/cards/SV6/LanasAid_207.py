from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import any_of, is_basic_energy_card, is_rule_box_free_pokemon

card = SupporterCardDef(
    guid="1e939ce9-4408-5b39-a37b-f873ae67b315",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LanasAid.Name",
    display_name="Lana's Aid",
    searchable_by=["Lana's Aid", "Supporter"],
    subtypes=["Supporter"],
    collector_number=207,
    set_code="SV6",
    rarity=Rarities.Rare,
    effect=recover_from_discard(any_of(is_rule_box_free_pokemon, is_basic_energy_card), count=3, to="hand")
)
