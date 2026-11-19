from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import (attack_effect_shield_passive,
                                                     is_in_active_spot)


def _benched(target, carrier):
    """(target, carrier) pred for the stadium shield: a Benched Pokemon.

    effects_blocked already refuses targets on the acting player's own side,
    so this covers "both yours and your opponent's" Benched Pokemon against
    the opposing player's attack and Ability effects."""
    return not is_in_active_spot(target)


card = StadiumCardDef(
    guid="18d84352-fc30-586e-ad24-a98ef26d8cb3",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleCage.Name",
    display_name="Battle Cage",
    searchable_by=["Battle Cage", "Stadium"],
    subtypes=["Stadium"],
    collector_number=116,
    set_code="ME2",
    rarity=Rarities.Rare,
    passive=attack_effect_shield_passive(_benched)
)
