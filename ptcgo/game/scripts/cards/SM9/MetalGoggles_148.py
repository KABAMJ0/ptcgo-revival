from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import carrier_pokemon, pokemon_of
from ptcgo.game.card_effects.passives_common import TakesLessPassive


_METAL = pokemon_of("metal")


def _metal_holder(target, carrier):
    """(target, carrier) pred: the Metal Pokemon this Tool is attached to."""
    return target is carrier_pokemon(carrier) and _METAL(target)


class MetalGogglesPassive(TakesLessPassive):
    """The two printed clauses on one Tool: -30 from opposing attacks (inherited
    from TakesLessPassive), and opposing attacks and Abilities can't put damage
    counters on the holder (the two effect-shield hooks).

    CombinedPassive forwards neither blocks_attack_effects nor
    blocks_ability_effects, so the shield has to ride the same object as the
    damage reduction rather than sit beside it."""

    def blocks_attack_effects(self, target, carrier, attacker=None, board=None):
        return bool(self.protects(target, carrier))

    def blocks_ability_effects(self, target, carrier):
        return bool(self.protects(target, carrier))


card = PokemonToolCardDef(
    guid="57d7e7f5-52e6-5255-af70-62d8d97943eb",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalGoggles.Name",
    display_name="Metal Goggles",
    searchable_by=["Metal Goggles", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=148,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    passive=MetalGogglesPassive(30, protects=_metal_holder)
)
