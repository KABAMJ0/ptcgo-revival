from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_card, reveal_hand_to_top_then_search

card = ItemCardDef(
    guid="591b3e73-8a9f-55ab-900c-9c42e842840c",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCommunication.Name",
    display_name="Pokémon Communication",
    searchable_by=["Pok\u00e9mon Communication", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    effect=reveal_hand_to_top_then_search(is_pokemon_card, is_pokemon_card)
)
