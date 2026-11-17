from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import attach_darkness_to_each_poison

card = SupporterCardDef(
    guid="3834b092-f2be-544e-83fd-a5e95029e6cb",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JaninesSecretArt.Name",
    display_name="Janine's Secret Art",
    searchable_by=["Janine's Secret Art", "Supporter"],
    subtypes=["Supporter"],
    collector_number=112,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    effect=attach_darkness_to_each_poison()
)
