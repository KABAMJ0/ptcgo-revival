from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import attach_discard_energy_each_then_draw, is_basic_energy_card

card = SupporterCardDef(
    guid="a6a4027a-c1a6-5c58-9f04-2368ff5dfa82",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorSadasVitality.Name",
    display_name="Professor Sada's Vitality",
    searchable_by=["Professor Sada's Vitality", "Supporter", "Ancient"],
    subtypes=["Supporter", "Ancient"],
    collector_number=120,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    effect=attach_discard_energy_each_then_draw(is_basic_energy_card, per_target=1, targets=2, draw=3)
)
