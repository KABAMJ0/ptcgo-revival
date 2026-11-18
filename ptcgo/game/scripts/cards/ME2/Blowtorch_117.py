from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import basic_energy_of, discard_opponent_attachment_or_stadium, hand_has

card = ItemCardDef(
    guid="bd9a621d-d209-5efc-afee-09b5d3deaefe",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Blowtorch.Name",
    display_name="Blowtorch",
    searchable_by=["Blowtorch", "Item"],
    subtypes=["Item"],
    collector_number=117,
    set_code="ME2",
    rarity=Rarities.Rare,
    effect=discard_opponent_attachment_or_stadium(basic_energy_of("fire"), "a basic Fire Energy"),
    condition=hand_has(basic_energy_of("fire"), 1)
)
