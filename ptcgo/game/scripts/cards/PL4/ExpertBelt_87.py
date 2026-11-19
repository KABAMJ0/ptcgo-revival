from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import hp_bonus_tool
from ptcgo.game.card_effects.trainers import holder_damage_boost, holder_prize_shift
from ptcgo.game.session.passives import Passive


class ExpertBeltPassive(Passive):
    """+20 HP, +20 damage to the opponent's Active, and 1 more Prize when the holder is Knocked Out."""

    def __init__(self):
        self._hp = hp_bonus_tool(20)
        self._boost = holder_damage_boost(20)
        self._prize = holder_prize_shift(1)

    def max_hp_bonus(self, pokemon, carrier):
        return self._hp.max_hp_bonus(pokemon, carrier)

    def modify_damage_dealt(self, calc, carrier):
        self._boost.modify_damage_dealt(calc, carrier)

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        return self._prize.modify_prizes_for_knockout(pokemon, ctx, count, carrier)


card = PokemonToolCardDef(
    guid="f6e78254-28b1-5ada-956c-5badc2a95faa",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ExpertBelt.Name",
    display_name="Expert Belt",
    searchable_by=["Expert Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=87,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    passive=ExpertBeltPassive(),
)
