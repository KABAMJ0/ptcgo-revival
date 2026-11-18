from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import extra_prize_on_ko, opponent_prizes_exactly, tera_attacker

card = SupporterCardDef(
    guid="d31cb4bd-0d28-5f0b-b36f-f93e7a3a857d",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Briar.Name",
    display_name="Briar",
    searchable_by=["Briar", "Supporter"],
    subtypes=["Supporter"],
    collector_number=171,
    set_code="SV7",
    rarity=Rarities.Rare,
    effect=extra_prize_on_ko(tera_attacker(), 1), condition=opponent_prizes_exactly(2)
)
