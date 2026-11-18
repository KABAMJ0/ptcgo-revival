from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_card, reveal_hand_to_top_then_search

card = ItemCardDef(
    guid="a56be50f-cbcd-52d4-bf26-809a91cafd03",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCommunication.Name",
    display_name="Pokémon Communication",
    searchable_by=["Pok\u00e9mon Communication", "Item"],
    subtypes=["Item"],
    collector_number=99,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=reveal_hand_to_top_then_search(is_pokemon_card, is_pokemon_card)
)
