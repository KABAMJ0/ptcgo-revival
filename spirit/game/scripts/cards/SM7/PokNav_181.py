from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import any_of, is_energy_card, is_pokemon_card

card = ItemCardDef(
    guid="457c7e1e-431b-5ea9-a9a2-aafba43a9d11",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokNav.Name",
    display_name="PokéNav",
    searchable_by=["Pok\u00e9Nav", "Item"],
    subtypes=["Item"],
    collector_number=181,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    effect=look_at_top(3, take=1, predicate=any_of(is_pokemon_card, is_energy_card), rest="back", minimum=0)
)
