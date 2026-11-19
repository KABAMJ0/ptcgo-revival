from ptcgo.game.card_effects.trainers import stop_poke_powers
from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="426a5188-2c95-5fe9-b899-3393674d10f8",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GoopGasAttack.Name",
    display_name="Goop Gas Attack",
    searchable_by=["Goop Gas Attack"],
    subtypes=[],
    collector_number=78,
    set_code="BASE5",
    rarity=Rarities.Common,
    effect=stop_poke_powers()
)
