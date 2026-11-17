from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect
from ptcgo.game.card_effects.trainers import choose_one, turn_damage_boost

card = SupporterCardDef(
    guid="df0f98f9-b058-544a-a2dd-c5f71f3f3f5f",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisScheme.Name",
    display_name="Giovanni's Scheme",
    searchable_by=["Giovanni's Scheme", "Supporter"],
    subtypes=["Supporter"],
    collector_number=138,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=choose_one([("Draw cards until you have 5 cards in your hand", draw_until_effect(5)), ("During this turn, your Pokémon's attacks do 20 more damage to your opp", turn_damage_boost(20))])
)
