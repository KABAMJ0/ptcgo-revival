from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import reveal_pokemon_then_search

card = ItemCardDef(
    guid="681c1ae2-9c08-5a42-a565-e968bb722190",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCommunication.Name",
    display_name="Pokémon Communication",
    searchable_by=["Pok\u00e9mon Communication", "Item"],
    subtypes=["Item"],
    collector_number=196,
    set_code="SM9",
    rarity=Rarities.RareSecret,
    effect=reveal_pokemon_then_search()
)
