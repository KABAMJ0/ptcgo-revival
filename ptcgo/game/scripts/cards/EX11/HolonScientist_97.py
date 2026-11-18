from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_until_not_behind, with_discard_cost

card = SupporterCardDef(
    guid="195a4523-8cb3-5d4f-94fa-3f77d04ac369",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonScientist.Name",
    display_name="Holon Scientist",
    searchable_by=["Holon Scientist", "Supporter"],
    subtypes=["Supporter"],
    collector_number=97,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, draw_until_not_behind())
)
