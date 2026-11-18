from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, pokemon_of, stadium_hp_bonus

card = StadiumCardDef(
    guid="f6ed8a60-ba95-5aeb-bac2-ee619b612f81",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LowPressureSystem.Name",
    display_name="Low Pressure System",
    searchable_by=["Low Pressure System", "Stadium"],
    subtypes=["Stadium"],
    collector_number=86,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    passive=stadium_hp_bonus(10, any_of(pokemon_of("grass"), pokemon_of("lightning")))
)
