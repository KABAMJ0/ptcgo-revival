from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_recover_either, is_basic_pokemon, is_evolution_pokemon

card = ItemCardDef(
    guid="5c8e39bb-40ac-5a2b-8dc4-8a6e77911cfd",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperRod.Name",
    display_name="Super Rod",
    searchable_by=["Super Rod"],
    subtypes=[],
    collector_number=103,
    set_code="NEO1",
    rarity=Rarities.Common,
    effect=flip_recover_either(is_evolution_pokemon, is_basic_pokemon)
)
