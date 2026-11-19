from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import SupporterCardDef, Ability, Triggers
from ptcgo.game.card_effects.trainers import misty_and_lorelei

card = SupporterCardDef(
    guid="b1b4db87-cec7-5c55-84e9-dc8425cca5ee",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistyLorelei.Name",
    display_name="Misty & Lorelei",
    searchable_by=["Misty & Lorelei", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=199,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=misty_and_lorelei,
)
