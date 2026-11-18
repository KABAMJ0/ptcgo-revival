from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of_subtype, stadium_hp_bonus

card = StadiumCardDef(
    guid="3b2b9d93-19af-5bdc-8b24-cc3e9a9fcff4",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IndigoPlateau.Name",
    display_name="Indigo Plateau",
    searchable_by=["Indigo Plateau", "Stadium"],
    subtypes=["Stadium"],
    collector_number=86,
    set_code="HGSS4",
    rarity=Rarities.Uncommon,
    passive=stadium_hp_bonus(30, pokemon_of_subtype('LEGEND'))
)
