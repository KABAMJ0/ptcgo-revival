from ptcgo.game.card_effects.trainers import gardenias_vigor
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="583f77bf-13c2-5252-a6fa-4ec073e62c09",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GardeniasVigor.Name",
    display_name="Gardenia's Vigor",
    searchable_by=["Gardenia's Vigor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=61,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareUltra,
    effect=gardenias_vigor
)
