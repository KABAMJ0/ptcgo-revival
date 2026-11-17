from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import extra_prize_on_ko, opponent_prizes_exactly, tera_attacker

card = SupporterCardDef(
    guid="f2a9c603-ea42-5e34-8553-65f99b9d9945",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Briar.Name",
    display_name="Briar",
    searchable_by=["Briar", "Supporter"],
    subtypes=["Supporter"],
    collector_number=100,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    effect=extra_prize_on_ko(tera_attacker(), 1), condition=opponent_prizes_exactly(2)
)
