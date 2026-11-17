from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import any_of, is_basic_energy_card, is_rule_box_free_pokemon

card = SupporterCardDef(
    guid="35297dea-07fd-57d7-9061-c861d7dddec7",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LanasAid.Name",
    display_name="Lana's Aid",
    searchable_by=["Lana's Aid", "Supporter"],
    subtypes=["Supporter"],
    collector_number=219,
    set_code="SV6",
    rarity=Rarities.Rare,
    effect=recover_from_discard(any_of(is_rule_box_free_pokemon, is_basic_energy_card), count=3, to="hand")
)
