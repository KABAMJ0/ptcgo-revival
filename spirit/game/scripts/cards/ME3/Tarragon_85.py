from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import all_of, basic_energy_of, pokemon_of

card = SupporterCardDef(
    guid="84621173-4cda-5ccb-ba88-9199aa37e3dd",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tarragon.Name",
    display_name="Tarragon",
    searchable_by=["Tarragon", "Supporter"],
    subtypes=["Supporter"],
    collector_number=85,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(all_of(pokemon_of("fighting"), basic_energy_of("fighting")), count=4, to="hand")
)
