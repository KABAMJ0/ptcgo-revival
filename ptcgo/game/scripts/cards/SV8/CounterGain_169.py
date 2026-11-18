from ptcgo.game.data_utils import PokemonToolCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_attack_discount

card = PokemonToolCardDef(
    guid="15f36567-294e-5228-8406-64340afd3780",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterGain.Name",
    display_name="Counter Gain",
    searchable_by=["Counter Gain", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=169,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    passive=holder_attack_discount(1, prize_behind=True)
)
