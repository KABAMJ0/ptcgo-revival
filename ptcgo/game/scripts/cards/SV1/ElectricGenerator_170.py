from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, basic_energy_of, excluding, is_in_active_spot, look_top_attach_up_to, pokemon_of

card = ItemCardDef(
    guid="cdf66ab1-eee4-508e-b3b0-5c09c6455f21",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ElectricGenerator.Name",
    display_name="Electric Generator",
    searchable_by=["Electric Generator", "Item"],
    subtypes=["Item"],
    collector_number=170,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    effect=look_top_attach_up_to(5, 2, predicate=basic_energy_of("lightning"), target_pred=all_of(excluding(is_in_active_spot), pokemon_of("lightning")))
)
