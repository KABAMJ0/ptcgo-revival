from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_supporter_card

card = ItemCardDef(
    guid="176e5110-fd93-5c42-ac41-09ef81ec482c",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokgear30.Name",
    display_name="Pokégear 3.0",
    searchable_by=["Pok\u00e9gear 3.0", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=is_supporter_card)
)
