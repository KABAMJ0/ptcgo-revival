from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_ability, is_special_energy, is_basic_energy_card
from ptcgo.game.card_effects.support_common import recover_from_discard

async def _power_tree(ctx):
    if any(is_special_energy(card) for card in ctx.discard_pile()):
        return
    await recover_from_discard(is_basic_energy_card, 1, reveal=True)(ctx)


card = StadiumCardDef(
    guid="062a4d57-2b14-50d6-a998-4207aa9cd370",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerTree.Name",
    display_name="Power Tree",
    searchable_by=["Power Tree", "Stadium"],
    subtypes=["Stadium"],
    collector_number=76,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Power Tree", _power_tree),
)
