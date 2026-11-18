from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import if_heads, is_pokemon_card

card = ItemCardDef(
    guid="f5d74c71-ac48-5827-9a21-f9094edf86b1",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=97,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=if_heads(search_to_hand(is_pokemon_card, count=1))
)
