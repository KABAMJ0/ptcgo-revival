from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import all_of, basic_energy_of, excluding, is_in_active_spot, pokemon_of

card = ItemCardDef(
    guid="6f13739e-b910-5ab1-841c-ddde84ebb3cd",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WondrousPatch.Name",
    display_name="Wondrous Patch",
    searchable_by=["Wondrous Patch", "Item"],
    subtypes=["Item"],
    collector_number=94,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    effect=attach_from_discard(basic_energy_of("psychic"), count=1, target=all_of(excluding(is_in_active_spot), pokemon_of("psychic")))
)
