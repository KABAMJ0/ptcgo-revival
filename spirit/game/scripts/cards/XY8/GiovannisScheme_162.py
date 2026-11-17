from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_until_effect
from spirit.game.card_effects.trainers import choose_one, turn_damage_boost

card = SupporterCardDef(
    guid="99f6a6a0-4d41-56f2-98ef-0bf1b59ab233",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisScheme.Name",
    display_name="Giovanni's Scheme",
    searchable_by=["Giovanni's Scheme", "Supporter"],
    subtypes=["Supporter"],
    collector_number=162,
    set_code="XY8",
    rarity=Rarities.RareUltra,
    effect=choose_one([("Draw cards until you have 5 cards in your hand", draw_until_effect(5)), ("During this turn, your Pokémon's attacks do 20 more damage to your opp", turn_damage_boost(20))])
)
