from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import extra_prize_on_ko, opponent_prizes_exactly, tera_attacker

card = SupporterCardDef(
    guid="2b1ffbcc-7da9-516c-b6d0-bd533f745ef5",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Briar.Name",
    display_name="Briar",
    searchable_by=["Briar", "Supporter"],
    subtypes=["Supporter"],
    collector_number=163,
    set_code="SV7",
    rarity=Rarities.Rare,
    effect=extra_prize_on_ko(tera_attacker(), 1), condition=opponent_prizes_exactly(2)
)
