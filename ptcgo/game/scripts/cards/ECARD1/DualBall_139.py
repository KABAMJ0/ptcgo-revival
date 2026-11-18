from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, excluding, flip_search_deck, is_basic_pokemon, pokemon_of_subtype

card = ItemCardDef(
    guid="e6f4e260-36e7-5ad7-95a4-a64421839dd8",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DualBall.Name",
    display_name="Dual Ball",
    searchable_by=["Dual Ball"],
    subtypes=[],
    collector_number=139,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=flip_search_deck(2, all_of(is_basic_pokemon, excluding(pokemon_of_subtype('Baby'))), 1)
)
