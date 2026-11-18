from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import all_of, basic_energy_of, excluding, is_in_active_spot, pokemon_of

card = ItemCardDef(
    guid="073d26a6-da8c-5445-ab3c-897f46bc25a2",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AquaPatch.Name",
    display_name="Aqua Patch",
    searchable_by=["Aqua Patch", "Item"],
    subtypes=["Item"],
    collector_number=119,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=attach_from_discard(basic_energy_of("water"), count=1, target=all_of(excluding(is_in_active_spot), pokemon_of("water")))
)
