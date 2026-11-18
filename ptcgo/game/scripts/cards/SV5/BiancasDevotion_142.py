from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_chosen

card = SupporterCardDef(
    guid="ac8f036b-069f-5396-ba3b-3449c4bbf9bb",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BiancasDevotion.Name",
    display_name="Bianca's Devotion",
    searchable_by=["Bianca's Devotion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=142,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    effect=heal_chosen(-1, count=1, hp_at_most=30)
)
