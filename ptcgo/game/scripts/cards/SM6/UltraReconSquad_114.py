from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_pred_draw_per, pokemon_of_subtype

card = SupporterCardDef(
    guid="4e341391-03da-5511-be85-f4b6f4381eb5",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraReconSquad.Name",
    display_name="Ultra Recon Squad",
    searchable_by=["Ultra Recon Squad", "Supporter"],
    subtypes=["Supporter"],
    collector_number=114,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    effect=discard_pred_draw_per(pokemon_of_subtype("Ultra Beast"), 2, 3)
)
