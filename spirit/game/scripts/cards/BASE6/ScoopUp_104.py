from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import devolve_to_basic

card = ItemCardDef(
    guid="d0d6eaf8-8b51-51d4-8a44-2edfb9a4f77b",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScoopUp.Name",
    display_name="Scoop Up",
    searchable_by=["Scoop Up"],
    subtypes=[],
    collector_number=104,
    set_code="BASE6",
    rarity=Rarities.Rare,
    effect=devolve_to_basic()
)
