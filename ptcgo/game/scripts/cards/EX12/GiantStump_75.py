from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.passives import Passive


class GiantStumpPassive(Passive):
    """Each player can't have more than 3 Benched Pokemon (the session's
    bench-capacity enforcement discards the excess, with everything attached,
    when this Stadium comes into play)."""

    def bench_capacity(self, player_id, carrier):
        return 3


card = StadiumCardDef(
    guid="3fd75fd0-ef97-5631-9870-02e27e2a7fb2",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiantStump.Name",
    display_name="Giant Stump",
    searchable_by=["Giant Stump", "Stadium"],
    subtypes=["Stadium"],
    collector_number=75,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    passive=GiantStumpPassive()
)
