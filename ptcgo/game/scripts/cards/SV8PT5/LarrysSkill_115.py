from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_then_search, is_basic_energy_card, is_pokemon_card, is_supporter_card

card = SupporterCardDef(
    guid="5ba70314-81c7-5dfb-a864-e054e92c2a07",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LarrysSkill.Name",
    display_name="Larry's Skill",
    searchable_by=["Larry's Skill", "Supporter"],
    subtypes=["Supporter"],
    collector_number=115,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    effect=discard_hand_then_search([is_pokemon_card, is_supporter_card, is_basic_energy_card])
)
