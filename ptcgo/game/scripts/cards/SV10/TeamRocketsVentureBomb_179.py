from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_counters_either

card = ItemCardDef(
    guid="5460e3d4-49af-5cb8-afd6-415e1e42a87b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsVentureBomb.Name",
    display_name="Team Rocket's Venture Bomb",
    searchable_by=["Team Rocket's Venture Bomb", "Item"],
    subtypes=["Item"],
    collector_number=179,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=flip_counters_either(2)
)
