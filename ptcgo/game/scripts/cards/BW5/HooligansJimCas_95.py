from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import if_heads, shuffle_random_from_opponent_hand

card = SupporterCardDef(
    guid="95b4b0c5-f29c-58a8-947b-27f88890b72a",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HooligansJimCas.Name",
    display_name="Hooligans Jim & Cas",
    searchable_by=["Hooligans Jim & Cas", "Supporter"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    effect=if_heads(shuffle_random_from_opponent_hand(3))
)
