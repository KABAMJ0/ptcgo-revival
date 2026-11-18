from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import takes_less_passive, pokemon_of, is_in_active_spot


def _colorless_active(target, carrier):
    return is_in_active_spot(target) and pokemon_of("colorless")(target)

card = StadiumCardDef(
    guid="4e066e60-33ce-58e7-9b45-653258aef9ce",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DrakesStadium.Name",
    display_name="Drake's Stadium",
    searchable_by=["Drake's Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=72,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    passive=takes_less_passive(10, protects=_colorless_active)
)
