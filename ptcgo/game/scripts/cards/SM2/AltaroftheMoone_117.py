from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import has_energy_of, stadium_retreat_shift

card = StadiumCardDef(
    guid="b1d91432-5568-55f2-bd79-723bd0422afe",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AltaroftheMoone.Name",
    display_name="Altar of the Moone",
    searchable_by=["Altar of the Moone", "Stadium"],
    subtypes=["Stadium"],
    collector_number=117,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    passive=stadium_retreat_shift(-2, has_energy_of("psychic", "darkness"))
)
