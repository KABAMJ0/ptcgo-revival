from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_named, stadium_hp_bonus

card = StadiumCardDef(
    guid="285d5abd-00ed-50d6-903c-6bd5fd3f1cc1",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsHideout.Name",
    display_name="Rocket's Hideout",
    searchable_by=["Rocket's Hideout", "Stadium"],
    subtypes=["Stadium"],
    collector_number=63,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    passive=stadium_hp_bonus(20, pokemon_named("dark"))
)
