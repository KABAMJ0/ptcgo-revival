from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import basic_energy_of, discard_opponent_attachment_or_stadium, hand_has

card = ItemCardDef(
    guid="0397f63f-37f4-5feb-bbdb-40d7cedd0414",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Blowtorch.Name",
    display_name="Blowtorch",
    searchable_by=["Blowtorch", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    effect=discard_opponent_attachment_or_stadium(basic_energy_of("fire"), "a basic Fire Energy"),
    condition=hand_has(basic_energy_of("fire"), 1)
)
