from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import gated_type, named_rule_box

card = PokemonToolCardDef(
    guid="f9522309-7180-549a-89b2-c895b0f158dd",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PsychicMemory.Name",
    display_name="Psychic Memory",
    searchable_by=["Psychic Memory", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=98,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    passive=gated_type("psychic", named_rule_box("silvally", "gx"))
)
