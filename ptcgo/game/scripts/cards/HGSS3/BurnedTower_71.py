from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_ability, flip_recover_basic_energy

card = StadiumCardDef(
    guid="cc04ff4f-1f85-5756-a89b-1280113a5999",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BurnedTower.Name",
    display_name="Burned Tower",
    searchable_by=["Burned Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=71,
    set_code="HGSS3",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Burned Tower", flip_recover_basic_energy(1)),
)
