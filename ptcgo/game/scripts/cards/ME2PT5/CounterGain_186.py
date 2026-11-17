from ptcgo.game.data_utils import PokemonToolCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_attack_discount

card = PokemonToolCardDef(
    guid="0febbc6e-bb4a-5c2b-b984-3bf22a322aef",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterGain.Name",
    display_name="Counter Gain",
    searchable_by=["Counter Gain", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=186,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    passive=holder_attack_discount(1, prize_behind=True)
)
