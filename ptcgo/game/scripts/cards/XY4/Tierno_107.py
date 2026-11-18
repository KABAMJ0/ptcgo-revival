from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n

card = SupporterCardDef(
    guid="29b0a32c-164d-51bc-9f42-b674e850bcee",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tierno.Name",
    display_name="Tierno",
    searchable_by=["Tierno", "Supporter"],
    subtypes=["Supporter"],
    collector_number=107,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    effect=draw_n(3)
)
