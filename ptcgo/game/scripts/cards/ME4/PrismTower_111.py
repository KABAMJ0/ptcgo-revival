from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_typed_from_hand_then, stadium_ability

card = StadiumCardDef(
    guid="3986a516-c004-5c65-9d2d-a6eaa15597fc",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PrismTower.Name",
    display_name="Prism Tower",
    searchable_by=["Prism Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=111,
    set_code="ME4",
    rarity=Rarities.Rare,
    ability=stadium_ability('Prism Tower', discard_typed_from_hand_then(None, 2, lambda ctx: ctx.draw_cards(1)))
)
