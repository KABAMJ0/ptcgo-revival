from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_search_deck, is_basic_energy_card

card = ItemCardDef(
    guid="67633335-3ee9-55b9-a277-d19f7bee9c65",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyArk.Name",
    display_name="Energy Ark",
    searchable_by=["Energy Ark"],
    subtypes=[],
    collector_number=75,
    set_code="NEO2",
    rarity=Rarities.Common,
    effect=flip_search_deck(2, is_basic_energy_card, 1)
)
