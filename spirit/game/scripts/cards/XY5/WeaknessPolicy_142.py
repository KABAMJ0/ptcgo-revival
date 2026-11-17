from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import holder_no_weakness

card = PokemonToolCardDef(
    guid="28f11837-2e45-543d-8ec7-428ff0440a43",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WeaknessPolicy.Name",
    display_name="Weakness Policy",
    searchable_by=["Weakness Policy", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=142,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    passive=holder_no_weakness()
)
