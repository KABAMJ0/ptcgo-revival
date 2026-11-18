from ptcgo.game.data_utils import PokemonToolCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_attack_discount

card = PokemonToolCardDef(
    guid="6b322b64-e418-57c9-9fda-e6e71425d449",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterGain.Name",
    display_name="Counter Gain",
    searchable_by=["Counter Gain", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=249,
    set_code="SV8",
    rarity=Rarities.Rare,
    passive=holder_attack_discount(1, prize_behind=True)
)
