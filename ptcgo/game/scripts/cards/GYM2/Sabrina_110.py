from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import move_all_energy_named

card = ItemCardDef(
    guid="7ea5ea75-851e-5c85-b8e3-3b6741381fb6",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sabrina.Name",
    display_name="Sabrina",
    searchable_by=["Sabrina"],
    subtypes=[],
    collector_number=110,
    set_code="GYM2",
    rarity=Rarities.Rare,
    effect=move_all_energy_named("sabrina")
)
