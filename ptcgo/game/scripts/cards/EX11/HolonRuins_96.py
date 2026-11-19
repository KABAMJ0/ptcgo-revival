from ptcgo.game.data_utils import StadiumCardDef, def_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_ability, draw_then_discard

async def _holon_ruins(ctx):
    if not any("δ" in (getattr(def_for(p.archetype_id), "display_name", "") or "")
               for p in ctx.my_pokemon_in_play()):
        return
    await draw_then_discard(1, 1)(ctx)


card = StadiumCardDef(
    guid="b6efba11-3e78-5137-97ef-4f0b39e28a3c",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonRuins.Name",
    display_name="Holon Ruins",
    searchable_by=["Holon Ruins", "Stadium"],
    subtypes=["Stadium"],
    collector_number=96,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Holon Ruins", _holon_ruins),
)
