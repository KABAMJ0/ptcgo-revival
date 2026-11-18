from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_hand_card_to_bottom, is_energy_card

card = ItemCardDef(
    guid="2eb5ba3a-6e28-56af-a897-a3059b45f176",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwatter.Name",
    display_name="Energy Swatter",
    searchable_by=["Energy Swatter", "Item"],
    subtypes=["Item"],
    collector_number=73,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    effect=opponent_hand_card_to_bottom(is_energy_card)
)
