from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n

card = SupporterCardDef(
    guid="f471107c-e923-58bd-830c-34517922bfad",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hau.Name",
    display_name="Hau",
    searchable_by=["Hau", "Supporter"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=draw_n(3)
)
