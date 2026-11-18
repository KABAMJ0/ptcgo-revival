from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import devolve_one, if_heads, stadium_ability

card = StadiumCardDef(
    guid="940dd877-bbd8-5fd1-ab4d-9590a4579952",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UnderseaRuins.Name",
    display_name="Undersea Ruins",
    searchable_by=["Undersea Ruins", "Stadium"],
    subtypes=["Stadium"],
    collector_number=138,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Undersea Ruins', if_heads(devolve_one(1)))
)
