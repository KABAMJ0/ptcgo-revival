from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_pokemon_card, recover_then_draw

card = SupporterCardDef(
    guid="dd476316-83a5-5636-bbd3-158b9a21d5be",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Miriam.Name",
    display_name="Miriam",
    searchable_by=["Miriam", "Supporter"],
    subtypes=["Supporter"],
    collector_number=238,
    set_code="SV1",
    rarity=Rarities.Rare,
    effect=recover_then_draw(is_pokemon_card, count=5, draw=3)
)
