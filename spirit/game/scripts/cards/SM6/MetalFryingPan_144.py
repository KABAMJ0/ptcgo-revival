from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import combined, holder_no_weakness, holder_takes_less

card = PokemonToolCardDef(
    guid="fa40153c-0cdf-521f-8e73-f1eb65f4814f",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalFryingPan.Name",
    display_name="Metal Frying Pan",
    searchable_by=["Metal Frying Pan", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=144,
    set_code="SM6",
    rarity=Rarities.RareSecret,
    passive=combined(combined(holder_takes_less(30), holder_no_weakness()))
)
