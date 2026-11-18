from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, card_named_contains, identity_swap_from_discard, is_pokemon_ex

card = ItemCardDef(
    guid="650a7443-8f64-500d-b829-cad59af7a209",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OgresMask.Name",
    display_name="Ogre's Mask",
    searchable_by=["Ogre's Mask", "Item"],
    subtypes=["Item"],
    collector_number=118,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    effect=identity_swap_from_discard(all_of(is_pokemon_ex, card_named_contains("ogerpon")))
)
