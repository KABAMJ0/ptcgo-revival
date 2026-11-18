from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.passives import Passive
from ptcgo.game.card_effects.passives_common import is_in_active_spot


class SkyPillarPassive(Passive):
    """Benched Pokemon (both sides) take no damage or effects from attacks."""

    def _benched(self, target):
        return target is not None and not is_in_active_spot(target)

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing and self._benched(calc.target))

    def blocks_attack_effects(self, target, carrier):
        return self._benched(target)


card = StadiumCardDef(
    guid="6b6b2fa4-989e-5220-9ea1-5610e33a303e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkyPillar.Name",
    display_name="Sky Pillar",
    searchable_by=["Sky Pillar", "Stadium"],
    subtypes=["Stadium"],
    collector_number=144,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    passive=SkyPillarPassive()
)
