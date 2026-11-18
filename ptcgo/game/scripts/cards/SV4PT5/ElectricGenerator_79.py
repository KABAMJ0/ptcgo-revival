from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, basic_energy_of, excluding, is_in_active_spot, look_top_attach_up_to, pokemon_of

card = ItemCardDef(
    guid="6ceff042-3abb-5c7d-910e-3d4ab76c7db5",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ElectricGenerator.Name",
    display_name="Electric Generator",
    searchable_by=["Electric Generator", "Item"],
    subtypes=["Item"],
    collector_number=79,
    set_code="SV4PT5",
    rarity=Rarities.Uncommon,
    effect=look_top_attach_up_to(5, 2, predicate=basic_energy_of("lightning"), target_pred=all_of(excluding(is_in_active_spot), pokemon_of("lightning")))
)
