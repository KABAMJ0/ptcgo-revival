from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_n_prize_bonus

card = SupporterCardDef(
    guid="7f6b402e-4ff5-5baf-a909-aee818cb4f9e",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EmceesHype.Name",
    display_name="Emcee's Hype",
    searchable_by=["Emcee's Hype", "Supporter"],
    subtypes=["Supporter"],
    collector_number=128,
    set_code="ME6",
    rarity=Rarities.Rare,
    effect=draw_n_prize_bonus(2, 2, 3)
)
