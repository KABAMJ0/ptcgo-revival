from ptcgo.game.data_utils import FossilItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="aaf07932-b23c-5bb4-b07e-6cc6ce100152",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SnorlaxDoll.Name",
    display_name="Snorlax Doll",
    searchable_by=["Snorlax Doll", "Item"],
    subtypes=["Item"],
    collector_number=175,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=120,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[fossil_discard_ability()],
)
card.prize_count = 0
