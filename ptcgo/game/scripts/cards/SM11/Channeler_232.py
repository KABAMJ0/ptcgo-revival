from ptcgo.game.card_effects.trainers import clear_attack_effects
from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="809692a1-a00e-5176-8900-c143eeca9d37",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Channeler.Name",
    display_name="Channeler",
    searchable_by=["Channeler", "Supporter"],
    subtypes=["Supporter"],
    collector_number=232,
    set_code="SM11",
    rarity=Rarities.RareUltra,
    effect=clear_attack_effects()
)
