from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, basic_energy_of, discard_typed_from_hand_then, stadium_ability

card = StadiumCardDef(
    guid="1f4f46e7-f9fc-525e-978b-5934d5dab812",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScorchedEarth.Name",
    display_name="Scorched Earth",
    searchable_by=["Scorched Earth", "Stadium"],
    subtypes=["Stadium"],
    collector_number=138,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Scorched Earth', discard_typed_from_hand_then(any_of(basic_energy_of("fire"), basic_energy_of("fighting")), 1, lambda ctx: ctx.draw_cards(2)))
)
