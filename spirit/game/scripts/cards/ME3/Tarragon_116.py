from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import all_of, basic_energy_of, pokemon_of

card = SupporterCardDef(
    guid="37c688e8-5abf-5254-9c5a-1fa3c5a53bdf",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tarragon.Name",
    display_name="Tarragon",
    searchable_by=["Tarragon", "Supporter"],
    subtypes=["Supporter"],
    collector_number=116,
    set_code="ME3",
    rarity=Rarities.Rare,
    effect=recover_from_discard(all_of(pokemon_of("fighting"), basic_energy_of("fighting")), count=4, to="hand")
)
