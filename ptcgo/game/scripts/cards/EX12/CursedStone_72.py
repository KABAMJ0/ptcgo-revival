from ptcgo.game.attributes import AttrID, Rarities
from ptcgo.game.data_utils import Ability, StadiumCardDef, Triggers
from ptcgo.game.session.passives import has_poke_power


async def cursed_stone_tick(ctx):
    """Each player puts 1 damage counter on each of their Poke-Power Pokemon."""
    for pokemon in ctx.my_pokemon_in_play():
        if not has_poke_power(pokemon):
            continue
        taken = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
        await ctx.set_damage_counters(pokemon, taken // 10 + 1)


card = StadiumCardDef(
    guid="e8bf4f78-75fa-56e8-8cf1-386a6fe3710a",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CursedStone.Name",
    display_name="Cursed Stone",
    searchable_by=["Cursed Stone", "Stadium"],
    subtypes=["Stadium"],
    collector_number=72,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Cursed Stone",
        game_text="At any time between turns, each player puts 1 damage counter "
                  "on his or her Pok\u00e9mon that has a Pok\u00e9-Power.",
        trigger=Triggers.BETWEEN_TURNS,
        effect=cursed_stone_tick,
    ),
)
