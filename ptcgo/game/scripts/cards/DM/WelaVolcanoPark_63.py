from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.passives import Passive


class _WelaBurnPark(Passive):
    """Burned is not removed when the between-turns recovery flip is heads."""

    def blocks_burn_recovery(self, pokemon, carrier):
        return True


card = StadiumCardDef(
    guid="dd8595de-b606-5d37-94d8-ce36fbed6758",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WelaVolcanoPark.Name",
    display_name="Wela Volcano Park",
    searchable_by=["Wela Volcano Park", "Stadium"],
    subtypes=["Stadium"],
    collector_number=63,
    set_code="DM",
    rarity=Rarities.Uncommon,
    passive=_WelaBurnPark(),
)
