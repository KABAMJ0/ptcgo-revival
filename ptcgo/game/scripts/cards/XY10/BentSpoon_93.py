from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import attack_effect_shield_passive

card = PokemonToolCardDef(
    guid="ca356f20-8348-56dc-8aa3-f650d36c0f43",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BentSpoon.Name",
    display_name="Bent Spoon",
    searchable_by=["Bent Spoon", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=93,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    passive=attack_effect_shield_passive()
)
