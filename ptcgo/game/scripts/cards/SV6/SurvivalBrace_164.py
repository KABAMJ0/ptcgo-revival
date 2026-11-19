from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import GutsSurvivePassive
from ptcgo.game.session.passives import carrier_pokemon


class SurvivalBracePassive(GutsSurvivePassive):
    """A holder at full HP survives the hit with 10 HP left, and the Tool that
    saved it is discarded ("Then, discard this card")."""

    def __init__(self):
        super().__init__(hp_floor=10, title="Survival Brace", flip=False,
                         require_full_hp=True)

    async def damage_interceptor(self, ctx, calc, target, carrier):
        survived = await super().damage_interceptor(ctx, calc, target, carrier)
        if survived is not None and carrier_pokemon(carrier) is not carrier:
            await ctx.discard_cards([carrier])
        return survived


card = PokemonToolCardDef(
    guid="caafae10-e30e-5ece-a8ae-1de60f3e39d0",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SurvivalBrace.Name",
    display_name="Survival Brace",
    searchable_by=["Survival Brace", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=164,
    set_code="SV6",
    rarity=Rarities.Rare,
    passive=SurvivalBracePassive()
)
