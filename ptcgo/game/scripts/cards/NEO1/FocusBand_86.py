from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import GutsSurvivePassive


class FocusBandPassive(GutsSurvivePassive):
    """Would be Knocked Out by an attack: flip a coin, and on heads the holder
    survives with 10 HP left and Focus Band is discarded."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        survived = await super().damage_interceptor(ctx, calc, target, carrier)
        if survived is not None:
            await ctx.discard_cards([carrier])
        return survived


card = PokemonToolCardDef(
    guid="eb76395f-e6b4-54b2-b5f9-052d16fa9b94",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FocusBand.Name",
    display_name="Focus Band",
    searchable_by=["Focus Band", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=86,
    set_code="NEO1",
    rarity=Rarities.Rare,
    passive=FocusBandPassive(hp_floor=10, title="Focus Band"),
)
