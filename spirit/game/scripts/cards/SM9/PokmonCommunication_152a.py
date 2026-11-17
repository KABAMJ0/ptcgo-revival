from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import reveal_pokemon_then_search

card = ItemCardDef(
    guid="19dc5821-cdcf-5193-ae36-2e2df7e52e87",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCommunication.Name",
    display_name="Pokémon Communication",
    searchable_by=["Pok\u00e9mon Communication", "Item"],
    subtypes=["Item"],
    collector_number=152,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=reveal_pokemon_then_search()
)
