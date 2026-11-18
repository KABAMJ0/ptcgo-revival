from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_typed_from_hand_then, is_energy_card

card = SupporterCardDef(
    guid="5a405e6b-190c-56bc-8893-eede555efb01",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EngineersAdjustments.Name",
    display_name="Engineer's Adjustments",
    searchable_by=["Engineer's Adjustments", "Supporter"],
    subtypes=["Supporter"],
    collector_number=75,
    set_code="HGSS2",
    rarity=Rarities.Uncommon,
    effect=discard_typed_from_hand_then(is_energy_card, 1, lambda ctx: ctx.draw_cards(4))
)
