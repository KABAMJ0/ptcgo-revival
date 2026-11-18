from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_shuffle_energy_into_deck

card = ItemCardDef(
    guid="56208084-623c-554a-821e-d1c9334e0ac6",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerCharge.Name",
    display_name="Power Charge",
    searchable_by=["Power Charge"],
    subtypes=[],
    collector_number=147,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=flip_shuffle_energy_into_deck(2)
)
