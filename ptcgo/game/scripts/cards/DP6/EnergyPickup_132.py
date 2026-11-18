from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_search_discard_attach, is_basic_energy_card

card = ItemCardDef(
    guid="fc33059c-0ec5-5d9c-bd5f-6c827a7fe105",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyPickup.Name",
    display_name="Energy Pickup",
    searchable_by=["Energy Pickup", "Item"],
    subtypes=["Item"],
    collector_number=132,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    effect=flip_search_discard_attach(1, is_basic_energy_card)
)
