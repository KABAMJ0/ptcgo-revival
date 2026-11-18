from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, pokemon_of, stadium_hp_bonus

card = StadiumCardDef(
    guid="7ad2a543-f166-5159-8471-289c581f147a",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LowPressureSystem.Name",
    display_name="Low Pressure System",
    searchable_by=["Low Pressure System", "Stadium"],
    subtypes=["Stadium"],
    collector_number=11,
    set_code="POP3",
    rarity=Rarities.Uncommon,
    passive=stadium_hp_bonus(10, any_of(pokemon_of("grass"), pokemon_of("lightning")))
)
