from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import guess_card_name

card = ItemCardDef(
    guid="d3fd7ce7-6607-59d5-bc72-de33ee0ef2e4",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesQuiz3.Name",
    display_name="Blaine's Quiz #3",
    searchable_by=["Blaine's Quiz #3"],
    subtypes=[],
    collector_number=112,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    effect=guess_card_name(3, attack_hint=True)
)
