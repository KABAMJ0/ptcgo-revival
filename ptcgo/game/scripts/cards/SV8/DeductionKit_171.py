from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import look_top_put_back

card = ItemCardDef(
    guid="19a5a6e2-2952-5b1d-8aff-26ac0780df26",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DeductionKit.Name",
    display_name="Deduction Kit",
    searchable_by=["Deduction Kit", "Item"],
    subtypes=["Item"],
    collector_number=171,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    effect=look_top_put_back(3)
)
