from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_takes_less_basic

card = PokemonToolCardDef(
    guid="f975ed78-41cc-5739-9a23-c063368516d7",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eviolite.Name",
    display_name="Eviolite",
    searchable_by=["Eviolite", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=91,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    passive=holder_takes_less_basic(20)
)
