from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import move_all_energy_named

card = ItemCardDef(
    guid="69ea82da-eaef-5520-9381-7ee0353710e6",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sabrina.Name",
    display_name="Sabrina",
    searchable_by=["Sabrina"],
    subtypes=[],
    collector_number=20,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    effect=move_all_energy_named("sabrina")
)
