from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.card_effects.passives_common import holder_has_energy_of, no_weakness_passive
from ptcgo.game.attributes import Rarities, PokemonTypes

card = StadiumCardDef(
    guid="afd45c1b-a248-5969-b353-fdc1f4061b38",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShadowCircle.Name",
    display_name="Shadow Circle",
    searchable_by=["Shadow Circle", "Stadium"],
    subtypes=["Stadium"],
    collector_number=126,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    passive=no_weakness_passive(protects=holder_has_energy_of(PokemonTypes.DARKNESS.value))
)
