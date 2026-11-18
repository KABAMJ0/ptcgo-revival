from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import all_of, basic_energy_of, excluding, is_in_active_spot, pokemon_of

card = ItemCardDef(
    guid="9fb81d10-cb62-52ca-97f8-af0e1ad772fe",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AquaPatch.Name",
    display_name="Aqua Patch",
    searchable_by=["Aqua Patch", "Item"],
    subtypes=["Item"],
    collector_number=161,
    set_code="SM2",
    rarity=Rarities.RareSecret,
    effect=attach_from_discard(basic_energy_of("water"), count=1, target=all_of(excluding(is_in_active_spot), pokemon_of("water")))
)
