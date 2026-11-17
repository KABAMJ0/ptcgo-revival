from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import basic_energy_of, stadium_ability

card = StadiumCardDef(
    guid="ad4a0423-2aa8-5470-b41b-48fb413e6e89",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Levincia.Name",
    display_name="Levincia",
    searchable_by=["Levincia", "Stadium"],
    subtypes=["Stadium"],
    collector_number=244,
    set_code="SV10",
    rarity=Rarities.Rare,
    ability=stadium_ability('Levincia', recover_from_discard(basic_energy_of("lightning"), count=2, to="hand"))
)
