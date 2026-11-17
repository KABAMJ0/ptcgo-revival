from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import heal_chosen

card = SupporterCardDef(
    guid="7d487257-554c-5297-9760-8563b32df5c1",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BiancasDevotion.Name",
    display_name="Bianca's Devotion",
    searchable_by=["Bianca's Devotion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=197,
    set_code="SV5",
    rarity=Rarities.Rare,
    effect=heal_chosen(-1, count=1, hp_at_most=30)
)
