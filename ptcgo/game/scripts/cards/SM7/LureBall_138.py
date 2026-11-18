from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_recover_to, is_evolution_pokemon

card = ItemCardDef(
    guid="ae5aff8d-6e25-5337-be44-b61d399090c0",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LureBall.Name",
    display_name="Lure Ball",
    searchable_by=["Lure Ball", "Item"],
    subtypes=["Item"],
    collector_number=138,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=flip_recover_to(3, is_evolution_pokemon, 1)
)
