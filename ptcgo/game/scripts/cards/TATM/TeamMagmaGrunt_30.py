from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import discard_then_draw
from ptcgo.game.card_effects.trainers import is_pokemon_card, team_magma_target

card = SupporterCardDef(
    guid="b70f88dd-ba84-5684-9ca6-03162b5b6181",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaGrunt.Name",
    display_name="Team Magma Grunt",
    searchable_by=["Team Magma Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=30,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    effect=discard_then_draw(1, lambda ctx, discarded: 3 + (
        1 if any(is_pokemon_card(card) and team_magma_target(card)
                 for card in discarded) else 0), optional=False)
)
