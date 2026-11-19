from ptcgo.game.data_utils import StadiumCardDef, unimplemented, def_for
from ptcgo.game.card_effects.passives_common import no_resistance_passive
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="deb0626a-251f-5250-8e39-76750dd7d088",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PewterCityGym.Name",
    display_name="Pewter City Gym",
    searchable_by=["Pewter City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=115,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    passive=no_resistance_passive(when=lambda calc, c: calc.attacker is not None and "brock" in (getattr(def_for(calc.attacker.archetype_id), "display_name", "") or "").lower())
)
