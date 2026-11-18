from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, any_of, discard_pred_draw_per, excluding, is_pokemon_EX, is_pokemon_card, is_pokemon_gx

card = SupporterCardDef(
    guid="82b11538-fc23-5c88-a138-4813890384d9",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Roxie.Name",
    display_name="Roxie",
    searchable_by=["Roxie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=205,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=discard_pred_draw_per(all_of(is_pokemon_card, excluding(any_of(is_pokemon_gx, is_pokemon_EX))), 2, 3)
)
