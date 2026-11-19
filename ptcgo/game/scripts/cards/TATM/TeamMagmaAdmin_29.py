from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_pokemon_card, team_magma_target

card = SupporterCardDef(
    guid="0a9d9923-ad43-56ca-9b2b-e2ffc812c8bc",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaAdmin.Name",
    display_name="Team Magma Admin",
    searchable_by=["Team Magma Admin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=29,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(lambda card: is_pokemon_card(card)
                                and team_magma_target(card), count=3, to="hand")
)
