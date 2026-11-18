from ptcgo.game.data_utils import StadiumCardDef, def_for
from ptcgo.game.attributes import Rarities, AttrID, PokemonTypes
from ptcgo.game.session.passives import Passive


class CinnabarGymPassive(Passive):
    """Ignore Weakness when a Water Pokemon damages a Pokemon with Blaine in its name."""

    def modify_weakness(self, calc, carrier):
        attacker, target = calc.attacker, calc.target
        if attacker is None or target is None:
            return
        if PokemonTypes.WATER.value not in (attacker.get_attribute(AttrID.POKEMON_TYPES) or []):
            return
        definition = def_for(target.archetype_id)
        if "blaine" in (getattr(definition, "display_name", "") or "").lower():
            calc.weakness_applies = False


card = StadiumCardDef(
    guid="c6be19f3-4b3c-5811-a8c8-ebda04595583",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CinnabarCityGym.Name",
    display_name="Cinnabar City Gym",
    searchable_by=["Cinnabar City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=113,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    passive=CinnabarGymPassive()
)
