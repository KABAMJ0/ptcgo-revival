from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import attacker_of_types, takes_less_from

card = PokemonToolCardDef(
    guid="f755d55b-27d3-5dbc-87f6-17ea6b487896",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PayapaBerry.Name",
    display_name="Payapa Berry",
    searchable_by=["Payapa Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=141,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    passive=takes_less_from(60, None, attacker_of_types("psychic"))
)
