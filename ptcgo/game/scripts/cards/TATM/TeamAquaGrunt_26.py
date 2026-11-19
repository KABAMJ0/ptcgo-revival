from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import discard_then_draw
from ptcgo.game.card_effects.trainers import is_pokemon_card, team_aqua_target

card = SupporterCardDef(
    guid="8f7dd117-d369-5ae5-8de7-598a8da25c9c",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaGrunt.Name",
    display_name="Team Aqua Grunt",
    searchable_by=["Team Aqua Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=26,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    effect=discard_then_draw(1, lambda ctx, discarded: 3 + (
        1 if any(is_pokemon_card(card) and team_aqua_target(card)
                 for card in discarded) else 0), optional=False)
)
