from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, pokemon_of, stadium_no_weakness

card = StadiumCardDef(
    guid="28c092f5-d671-5e44-9cd2-70284abb38a9",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AltaroftheSunne.Name",
    display_name="Altar of the Sunne",
    searchable_by=["Altar of the Sunne", "Stadium"],
    subtypes=["Stadium"],
    collector_number=118,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    passive=stadium_no_weakness(any_of(pokemon_of("fire"), pokemon_of("metal")))
)
