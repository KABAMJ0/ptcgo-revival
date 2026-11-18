from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_then_search, is_basic_energy_card, is_pokemon_card, is_supporter_card

card = SupporterCardDef(
    guid="fabf1406-9ee9-5fb6-bedc-eb6e170faffb",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LarrysSkill.Name",
    display_name="Larry's Skill",
    searchable_by=["Larry's Skill", "Supporter"],
    subtypes=["Supporter"],
    collector_number=139,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=discard_hand_then_search([is_pokemon_card, is_supporter_card, is_basic_energy_card])
)
