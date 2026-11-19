from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.card_effects.passives_common import previous_evolution_grant_passive
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="23a9102a-c29c-510f-a38e-8d8488f7a361",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShrineofMemories.Name",
    display_name="Shrine of Memories",
    searchable_by=["Shrine of Memories", "Stadium"],
    subtypes=["Stadium"],
    collector_number=139,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    passive=previous_evolution_grant_passive()
)
