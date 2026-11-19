from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.passives_common import no_resistance_passive, pokemon_of_types
from ptcgo.game.card_effects.trainers import stadium_no_weakness
from ptcgo.game.session.passives import Passive


_LIGHTNING = pokemon_of_types(PokemonTypes.LIGHTNING.value)
_NO_RESISTANCE = no_resistance_passive(
    when=lambda calc, carrier: calc.attacker is not None and _LIGHTNING(calc.attacker))
_NO_WEAKNESS = stadium_no_weakness(_LIGHTNING)


class SunyshoreCityGymPassive(Passive):
    """Lightning attacks ignore Resistance; every Lightning Pokemon has no Weakness."""

    def modify_resistance(self, calc, carrier):
        _NO_RESISTANCE.modify_resistance(calc, carrier)

    def modify_weakness(self, calc, carrier):
        _NO_WEAKNESS.modify_weakness(calc, carrier)


card = StadiumCardDef(
    guid="8dc7cd8e-792f-50af-a796-10c99749b6d6",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SunyshoreCityGym.Name",
    display_name="Sunyshore City Gym",
    searchable_by=["Sunyshore City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    passive=SunyshoreCityGymPassive(),
)
