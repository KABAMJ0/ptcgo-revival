from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import combined, holder_no_weakness, holder_takes_less

card = PokemonToolCardDef(
    guid="52b2b3ca-fdbd-5761-874f-87ec4c16bcf2",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalFryingPan.Name",
    display_name="Metal Frying Pan",
    searchable_by=["Metal Frying Pan", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=112,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    passive=combined(combined(holder_takes_less(30, protect_type="metal"), holder_no_weakness(protect_type="metal")))
)
