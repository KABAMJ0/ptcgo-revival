from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import powerglass_end_of_turn

card = PokemonToolCardDef(
    guid="61165989-a362-56cb-a76b-0ab4d5e4a53f",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Powerglass.Name",
    display_name="Powerglass",
    searchable_by=["Powerglass", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=97,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    granted_abilities=powerglass_end_of_turn('Powerglass')
)
