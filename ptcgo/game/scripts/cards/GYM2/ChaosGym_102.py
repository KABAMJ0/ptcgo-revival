from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.card_effects.passives_common import trainer_play_flip_passive
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="f45119ca-e810-56fa-8944-a81b092242ea",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChaosGym.Name",
    display_name="Chaos Gym",
    searchable_by=["Chaos Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=102,
    set_code="GYM2",
    rarity=Rarities.Rare,
    passive=trainer_play_flip_passive()
)
