from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, basic_energy_of, discard_typed_from_hand_then, stadium_ability

card = StadiumCardDef(
    guid="f7889519-a4be-59dc-9f00-5dc4bfac83af",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScorchedEarth.Name",
    display_name="Scorched Earth",
    searchable_by=["Scorched Earth", "Stadium"],
    subtypes=["Stadium"],
    collector_number=110,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Scorched Earth', discard_typed_from_hand_then(any_of(basic_energy_of("fire"), basic_energy_of("fighting")), 1, lambda ctx: ctx.draw_cards(2)))
)
