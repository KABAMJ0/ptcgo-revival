from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_pred_draw_per, pokemon_of_subtype

card = SupporterCardDef(
    guid="c09dd4bc-6c3f-50c1-ac9b-32d90a284c16",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraReconSquad.Name",
    display_name="Ultra Recon Squad",
    searchable_by=["Ultra Recon Squad", "Supporter"],
    subtypes=["Supporter"],
    collector_number=131,
    set_code="SM6",
    rarity=Rarities.RareUltra,
    effect=discard_pred_draw_per(pokemon_of_subtype("Ultra Beast"), 2, 3)
)
