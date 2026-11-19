from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities, AttrID, PokemonTypes
from ptcgo.game.card_effects.passives_common import no_resistance_passive


def _psychic_or_fighting_attacker(calc, carrier):
    attacker = calc.attacker
    if attacker is None:
        return False
    types = set(attacker.get_attribute(AttrID.POKEMON_TYPES) or [])
    return bool(types & {PokemonTypes.PSYCHIC.value, PokemonTypes.FIGHTING.value})

card = StadiumCardDef(
    guid="559444fd-2fd8-5ce1-ad6a-0c3eaeb7cb01",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MagneticStorm.Name",
    display_name="Magnetic Storm",
    searchable_by=["Magnetic Storm", "Stadium"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    passive=no_resistance_passive(when=_psychic_or_fighting_attacker)
)
