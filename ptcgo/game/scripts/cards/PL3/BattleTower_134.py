from ptcgo.game.data_utils import StadiumCardDef, subtypes_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.passives import Passive


class _BattleTowerPassive(Passive):
    """Any player's level-up removes 4 damage counters (40 damage) from the
    Pokemon that levelled up. Evolutions are not level-ups."""

    def heal_on_evolve(self, evolved, pre_evolution, player_id, carrier):
        if "Level-Up" not in (subtypes_for(evolved.archetype_id) or []):
            return 0
        return 40



card = StadiumCardDef(
    guid="c384186b-499d-53bc-8eb9-1aad980384f9",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleTower.Name",
    display_name="Battle Tower",
    searchable_by=["Battle Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=134,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    passive=_BattleTowerPassive(),
)
