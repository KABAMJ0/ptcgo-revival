from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_until_tails_draw

card = SupporterCardDef(
    guid="91e720d8-9311-56cb-ae4e-b30e4218c729",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MarysImpulse.Name",
    display_name="Mary's Impulse",
    searchable_by=["Mary's Impulse", "Supporter"],
    subtypes=["Supporter"],
    collector_number=142,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=flip_until_tails_draw(2)
)
