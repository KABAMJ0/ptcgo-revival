from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import all_of, hop, is_basic_pokemon, named

card = ItemCardDef(
    guid="2fbdb90b-a0ef-5d6c-822e-3aeee11b7e8e",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HopsBag.Name",
    display_name="Hop's Bag",
    searchable_by=["Hop's Bag", "Item"],
    subtypes=["Item"],
    collector_number=147,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(all_of(is_basic_pokemon, named("hop")), 2)
)
