from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_from_deck_matching, is_pokemon_gx

card = SupporterCardDef(
    guid="cb8c5531-c0bb-5f15-b2e5-0095e1fcb873",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedBlue.Name",
    display_name="Red & Blue",
    searchable_by=["Red & Blue", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=202,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=evolve_from_deck_matching(is_pokemon_gx)
)
