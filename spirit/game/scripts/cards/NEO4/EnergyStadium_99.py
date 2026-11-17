from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import if_heads, is_basic_energy_card, stadium_ability

card = StadiumCardDef(
    guid="02b0c11b-06d6-5bc7-9ee6-e920ed4bbda5",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyStadium.Name",
    display_name="Energy Stadium",
    searchable_by=["Energy Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=99,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Energy Stadium', if_heads(recover_from_discard(is_basic_energy_card, count=1, to="hand")))
)
