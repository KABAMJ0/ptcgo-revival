from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_from_opponent_hand, is_energy_card

card = SupporterCardDef(
    guid="d8b2f21a-fa75-59be-8458-4822b9066cd8",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamSkullGrunt.Name",
    display_name="Team Skull Grunt",
    searchable_by=["Team Skull Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SM1",
    rarity=Rarities.RareUltra,
    effect=discard_from_opponent_hand(predicate=is_energy_card, count=2)
)
