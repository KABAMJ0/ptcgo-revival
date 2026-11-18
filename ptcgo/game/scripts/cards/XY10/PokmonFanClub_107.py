from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_basic_pokemon

card = SupporterCardDef(
    guid="2cbda0aa-4cf8-523d-80f3-3e5f2417a63c",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonFanClub.Name",
    display_name="Pokémon Fan Club",
    searchable_by=["Pok\u00e9mon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=107,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_basic_pokemon, count=2)
)
