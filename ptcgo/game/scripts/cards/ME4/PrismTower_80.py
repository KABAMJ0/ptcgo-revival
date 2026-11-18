from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_typed_from_hand_then, stadium_ability

card = StadiumCardDef(
    guid="b858c975-bc9e-5532-abe3-f34868d55237",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PrismTower.Name",
    display_name="Prism Tower",
    searchable_by=["Prism Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=80,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Prism Tower', discard_typed_from_hand_then(None, 2, lambda ctx: ctx.draw_cards(1)))
)
