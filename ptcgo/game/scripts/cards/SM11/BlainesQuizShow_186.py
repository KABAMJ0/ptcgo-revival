from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import guess_card_name

card = SupporterCardDef(
    guid="a8f982cb-3831-5788-97f0-2abb7064c632",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesQuizShow.Name",
    display_name="Blaine's Quiz Show",
    searchable_by=["Blaine's Quiz Show", "Supporter"],
    subtypes=["Supporter"],
    collector_number=186,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    effect=guess_card_name(4, attack_hint=True)
)
