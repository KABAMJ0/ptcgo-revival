from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import active_is_water_or_metal, cyrus_two_benched

card = SupporterCardDef(
    guid="4e7ff502-56ef-5e9c-aaaf-42e068e827a4",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cyrus.Name",
    display_name="Cyrus ◇",
    searchable_by=["Cyrus \u25c7", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=120,
    set_code="SM5",
    rarity=Rarities.Rare,
    effect=cyrus_two_benched(),
    condition=active_is_water_or_metal()
)
