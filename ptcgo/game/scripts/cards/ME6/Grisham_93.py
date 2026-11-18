from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_where

card = SupporterCardDef(
    guid="78792c43-0ab1-5730-86ff-967303c0df2f",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Grisham.Name",
    display_name="Grisham",
    searchable_by=["Grisham", "Supporter"],
    subtypes=["Supporter"],
    collector_number=93,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    effect=heal_where(50, "each_both")
)
