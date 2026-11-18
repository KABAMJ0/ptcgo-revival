from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_hp_bonus, pokemon_of

card = StadiumCardDef(
    guid="325e1feb-7c9c-53cc-bb9a-290e604ea12c",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AspertiaCityGym.Name",
    display_name="Aspertia City Gym",
    searchable_by=["Aspertia City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=127,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    passive=stadium_hp_bonus(20, pokemon_of("colorless"))
)
