from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    card_named_contains, fossil_search, stadium_ability,
)

card = StadiumCardDef(
    guid="969b4c1d-8cec-5939-9ffc-a80d4237debf",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilQuarry.Name",
    display_name="Fossil Quarry",
    searchable_by=["Fossil Quarry", "Stadium"],
    subtypes=["Stadium"],
    collector_number=76,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    ability=stadium_ability(
        "Fossil Quarry",
        fossil_search(card_named_contains("Antique"), 2, "Antique Fossil"),
    ),
)
