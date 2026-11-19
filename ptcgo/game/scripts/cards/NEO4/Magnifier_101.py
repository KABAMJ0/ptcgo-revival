from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import no_resistance_for_turn

card = ItemCardDef(
    guid="8e7c9327-face-5c1f-9331-1083aa0b9a10",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Magnifier.Name",
    display_name="Magnifier",
    searchable_by=["Magnifier"],
    subtypes=[],
    collector_number=101,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    effect=no_resistance_for_turn()
)
