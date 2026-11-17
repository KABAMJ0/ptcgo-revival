from ptcgo.game.data_utils import PokemonToolCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_damage_boost

card = PokemonToolCardDef(
    guid="80e07131-c5de-5aa2-9077-42d702d02f56",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MuscleBand.Name",
    display_name="Muscle Band",
    searchable_by=["Muscle Band", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=121,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    passive=holder_damage_boost(20)
)
