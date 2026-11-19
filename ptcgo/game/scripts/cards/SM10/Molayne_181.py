from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_has, is_metal_energy_card, molayne

card = SupporterCardDef(
    guid="dfe1a87f-2507-5d8a-a85b-5e03f17d3f63",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Molayne.Name",
    display_name="Molayne",
    searchable_by=["Molayne", "Supporter"],
    subtypes=["Supporter"],
    collector_number=181,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=molayne(),
    condition=hand_has(is_metal_energy_card, 2)
)
