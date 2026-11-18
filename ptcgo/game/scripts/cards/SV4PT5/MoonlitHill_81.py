from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import basic_energy_of, discard_typed_from_hand_then, heal_where, stadium_ability

card = StadiumCardDef(
    guid="7a3a1e37-bc5d-5013-97ab-eb2d8be9d33c",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MoonlitHill.Name",
    display_name="Moonlit Hill",
    searchable_by=["Moonlit Hill", "Stadium"],
    subtypes=["Stadium"],
    collector_number=81,
    set_code="SV4PT5",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Moonlit Hill', discard_typed_from_hand_then(basic_energy_of("psychic"), 1, heal_where(30, "each_own")))
)
