from ptcgo.game.data_utils import SupporterCardDef, def_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_card
from ptcgo.game.card_effects.support_common import requires_hand

async def _team_aqua_schemer(ctx):
    pool = [card for card in ctx.hand() if is_pokemon_card(card)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1, minimum=1, prompt="Choose a Pokémon to discard")
    if not picks:
        return
    name = (getattr(def_for(picks[0].archetype_id), "display_name", "") or "").lower()
    await ctx.discard_cards(picks)
    await ctx.draw_cards(4 if "team aqua" in name else 3)


card = SupporterCardDef(
    guid="755aee45-0ba8-5bab-bc47-f3faf4638fec",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaSchemer.Name",
    display_name="Team Aqua Schemer",
    searchable_by=["Team Aqua Schemer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=69,
    set_code="EX4",
    rarity=Rarities.Common,
    effect=_team_aqua_schemer,
    condition=requires_hand(is_pokemon_card, 1),
)
