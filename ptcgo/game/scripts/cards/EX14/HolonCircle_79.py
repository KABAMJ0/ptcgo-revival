from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.passives import Passive


class HolonCirclePassive(Passive):
    """No attack by an Active Pokemon does anything, and the first one that
    is used takes this card down with it."""

    def __init__(self):
        self.attack_followup = self._discard_self

    def prevents_damage(self, calc, carrier) -> bool:
        return calc.is_attack

    def blocks_attack_effects(self, target, carrier, attacker=None, board=None) -> bool:
        return True

    async def _discard_self(self, ctx, carrier) -> None:
        await ctx.discard_stadium()


card = StadiumCardDef(
    guid="d6e83b9b-8fce-5f14-bf59-35ad8e4b809d",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonCircle.Name",
    display_name="Holon Circle",
    searchable_by=["Holon Circle", "Stadium"],
    subtypes=["Stadium"],
    collector_number=79,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    passive=HolonCirclePassive(),
)
