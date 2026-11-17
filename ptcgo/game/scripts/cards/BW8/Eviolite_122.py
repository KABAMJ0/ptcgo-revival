from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_takes_less_basic

card = PokemonToolCardDef(
    guid="f12b4481-2161-555d-83ee-288d7d417128",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eviolite.Name",
    display_name="Eviolite",
    searchable_by=["Eviolite", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=122,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    passive=holder_takes_less_basic(20)
)
