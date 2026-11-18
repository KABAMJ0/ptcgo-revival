from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import move_energy_of_type_between, stadium_ability

card = StadiumCardDef(
    guid="5a1c2410-eb89-569e-9709-ba7f582a1d06",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StarkMountain.Name",
    display_name="Stark Mountain",
    searchable_by=["Stark Mountain", "Stadium"],
    subtypes=["Stadium"],
    collector_number=135,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Stark Mountain', move_energy_of_type_between("fire", "fighting"))
)
