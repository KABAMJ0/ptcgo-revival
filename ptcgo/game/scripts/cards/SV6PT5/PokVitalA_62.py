from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item

card = ItemCardDef(
    guid="5fc1a94e-0f9e-5c77-889f-58a35c513c8b",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokVitalA.Name",
    display_name="Poké Vital A",
    searchable_by=["Pok\u00e9 Vital A", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=62,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    effect=heal_item(amount=150, scope="choice")
)
