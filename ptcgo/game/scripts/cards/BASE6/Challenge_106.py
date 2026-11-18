from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import challenge_opponent

card = ItemCardDef(
    guid="c1374ece-0e52-5734-8061-b464472838ca",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Challenge.Name",
    display_name="Challenge!",
    searchable_by=["Challenge!"],
    subtypes=[],
    collector_number=106,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    effect=challenge_opponent(2)
)
