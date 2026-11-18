from ptcgo.game.data_utils import StadiumCardDef, def_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.passives import Passive


class HolonLegacyPassive(Passive):
    """Pokemon printed with the delta marker have no Weakness and no Abilities."""

    def _delta(self, pokemon):
        definition = def_for(pokemon.archetype_id)
        return "\u03b4" in (getattr(definition, "display_name", "") or "")

    def modify_weakness(self, calc, carrier):
        if calc.target is not None and self._delta(calc.target):
            calc.weakness_applies = False

    def blocks_abilities(self, pokemon, carrier):
        return self._delta(pokemon)


card = StadiumCardDef(
    guid="88e3ed0a-012e-5bbb-8005-f080c9b86d5b",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonLegacy.Name",
    display_name="Holon Legacy",
    searchable_by=["Holon Legacy", "Stadium"],
    subtypes=["Stadium"],
    collector_number=74,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    passive=HolonLegacyPassive()
)
