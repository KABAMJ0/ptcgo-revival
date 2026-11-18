from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import GutsSurvivePassive
from ptcgo.game.card_effects.trainers import pokemon_of
from ptcgo.game.session.passives import carrier_pokemon


class FocusSashPassive(GutsSurvivePassive):
    """The Fighting holder survives a KO at full HP with 10 HP left, and the
    Tool that saved it is discarded ("Then, discard this card")."""

    def __init__(self):
        super().__init__(hp_floor=10, title="Focus Sash", flip=False,
                         require_full_hp=True)
        self.holder = pokemon_of("fighting")

    async def damage_interceptor(self, ctx, calc, target, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or not self.holder(holder):
            return None
        survived = await super().damage_interceptor(ctx, calc, target, carrier)
        if survived is not None and carrier is not holder:
            await ctx.discard_cards([carrier])
        return survived


card = PokemonToolCardDef(
    guid="aa83f6fc-449f-5100-9633-a1ff5d59271f",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FocusSash.Name",
    display_name="Focus Sash",
    searchable_by=["Focus Sash", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=91,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    passive=FocusSashPassive()
)
