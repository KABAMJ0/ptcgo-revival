from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import PokemonTypes
from ptcgo.game.card_effects.passives_common import no_resistance_passive, pokemon_of_types
from ptcgo.game.attributes import AttrID, PokemonTypes
from ptcgo.game.attributes import Rarities

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
    passive=no_resistance_passive(when=lambda calc, c: calc.attacker is not None and pokemon_of_types(PokemonTypes.PSYCHIC.value, PokemonTypes.FIGHTING.value)(calc.attacker))
)
