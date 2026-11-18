from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities, AttrID
from ptcgo.game.session.passives import Passive


class CrystalBeachPassive(Passive):
    """Special Energy that provides 2 or more Energy provides only 1 Colorless.

    `suppresses_special_energy` sends the card to the engine's one-Colorless
    provision (`session/passives.py:1083`), so the predicate only has to pick
    the energies the text names.
    """

    def suppresses_special_energy(self, energy, carrier):
        info = energy.get_attribute(AttrID.ENERGY_INFO) or {}
        return any(len(option) >= 2 for option in info.get("options", []))


card = StadiumCardDef(
    guid="c0f1f75e-b36f-5dfa-ba42-791f4f99283e",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalBeach.Name",
    display_name="Crystal Beach",
    searchable_by=["Crystal Beach", "Stadium"],
    subtypes=["Stadium"],
    collector_number=75,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    passive=CrystalBeachPassive()
)
