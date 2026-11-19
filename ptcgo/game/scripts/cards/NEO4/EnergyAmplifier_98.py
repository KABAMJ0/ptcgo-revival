from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_energy_to_deck_then_flip_search

card = ItemCardDef(
    guid="a88e1551-714b-5896-9da4-eeecb122d0c4",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyAmplifier.Name",
    display_name="Energy Amplifier",
    searchable_by=["Energy Amplifier"],
    subtypes=[],
    collector_number=98,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    effect=hand_energy_to_deck_then_flip_search(3)
)
