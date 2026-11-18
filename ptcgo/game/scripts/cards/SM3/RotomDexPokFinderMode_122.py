from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import look_top_reorder_or_shuffle

card = ItemCardDef(
    guid="21dff0ef-6275-5b93-b3eb-171cd14943b8",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RotomDexPokFinderMode.Name",
    display_name="Rotom Dex Poké Finder Mode",
    searchable_by=["Rotom Dex Pok\u00e9 Finder Mode", "Item"],
    subtypes=["Item"],
    collector_number=122,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=look_top_reorder_or_shuffle(4)
)
