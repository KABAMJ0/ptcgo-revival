from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.card_effects.passives_common import retreat_flip_passive
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="c77b709b-b991-5a70-90ac-9a1f25b18c58",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MirageStadium.Name",
    display_name="Mirage Stadium",
    searchable_by=["Mirage Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=132,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    passive=retreat_flip_passive()
)
