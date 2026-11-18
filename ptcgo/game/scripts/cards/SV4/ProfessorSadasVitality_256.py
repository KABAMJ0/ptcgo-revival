from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import attach_discard_energy_each_then_draw, is_basic_energy_card, pokemon_of_subtype

card = SupporterCardDef(
    guid="fbc6bba7-4813-58ec-b324-d29894771394",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorSadasVitality.Name",
    display_name="Professor Sada's Vitality",
    searchable_by=["Professor Sada's Vitality", "Supporter", "Ancient"],
    subtypes=["Supporter", "Ancient"],
    collector_number=256,
    set_code="SV4",
    rarity=Rarities.Rare,
    effect=attach_discard_energy_each_then_draw(is_basic_energy_card, per_target=1, targets=2, draw=3, target_pred=pokemon_of_subtype("Ancient"))
)
