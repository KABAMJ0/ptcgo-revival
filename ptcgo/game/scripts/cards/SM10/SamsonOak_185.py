from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_if_same_active_type

card = SupporterCardDef(
    guid="23e345e9-9e38-5bdd-8e07-46ddf59d6d1e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SamsonOak.Name",
    display_name="Samson Oak",
    searchable_by=["Samson Oak", "Supporter"],
    subtypes=["Supporter"],
    collector_number=185,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=draw_if_same_active_type(2, 2)
)
