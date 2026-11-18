from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_pokemon, stadium_retreat_shift

card = StadiumCardDef(
    guid="eef9d804-c6b4-51c2-bdfa-36e5d22b410b",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkyarrowBridge.Name",
    display_name="Skyarrow Bridge",
    searchable_by=["Skyarrow Bridge", "Stadium"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    passive=stadium_retreat_shift(-1, is_basic_pokemon)
)
