from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import pokemon_of_subtype

card = ItemCardDef(
    guid="1b3890d6-4786-5fe6-aa3e-8afc54ada2e2",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamPlasmaBall.Name",
    display_name="Team Plasma Ball",
    searchable_by=["Team Plasma Ball", "Item", "Team Plasma"],
    subtypes=["Item", "Team Plasma"],
    collector_number=105,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(pokemon_of_subtype("Team Plasma"), count=1)
)
