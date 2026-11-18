from ptcgo.game.data_utils import PokemonToolCardDef, Attack, def_for
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card


def _cap_holders(ctx):
    return [pokemon for tool, pokemon in ctx.tools_in_play()
            if pokemon.owning_player_id == ctx.player_id
            and (getattr(def_for(tool.archetype_id), "display_name", "") or "")
            == "Mega Rayquaza Cap"]


async def delta_gift(ctx):
    for pokemon in _cap_holders(ctx):
        holder_name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
        picks = await ctx.search_deck(
            is_basic_energy_card, count=1, minimum=0,
            prompt=f"Choose a Basic Energy card for {holder_name}")
        if picks:
            await ctx.attach_energy(picks[0], pokemon)
    await ctx.shuffle_deck()


card = PokemonToolCardDef(
    guid="2ddcd2a7-10c2-5a7f-94d8-11db53a25ada",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegaRayquazaCap.Name",
    display_name="Mega Rayquaza Cap",
    searchable_by=["Mega Rayquaza Cap", "MEGA", "Pok\u00e9mon Tool"],
    subtypes=["MEGA", "Pok\u00e9mon Tool"],
    collector_number=100,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Delta Gift",
            game_text="For each of your Pok\u00e9mon that has a Mega Rayquaza Cap "
                      "attached, search your deck for a Basic Energy card and attach "
                      "it to that Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=delta_gift,
        ),
    ],
)
