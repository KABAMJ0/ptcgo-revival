from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import copycat_draw

card = SupporterCardDef(
    guid="d256b5ed-7e16-582d-9828-0e8f68580918",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Copycat.Name",
    display_name="Copycat",
    searchable_by=["Copycat", "Supporter"],
    subtypes=["Supporter"],
    collector_number=163,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    effect=copycat_draw()
)
