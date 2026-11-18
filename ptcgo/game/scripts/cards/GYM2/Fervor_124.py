from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import basic_energy_of

card = ItemCardDef(
    guid="952e2151-0c0c-5086-8a5d-323e6e1cdc2a",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fervor.Name",
    display_name="Fervor",
    searchable_by=["Fervor"],
    subtypes=[],
    collector_number=124,
    set_code="GYM2",
    rarity=Rarities.Common,
    effect=look_at_top(3, take=3, predicate=basic_energy_of("fire"), rest="discard", minimum=0)
)
