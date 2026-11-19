from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

async def magical_echo(ctx):
    """Move all damage counters from 1 of your Benched Pokemon to the opponent's Active."""
    damaged = [p for p in ctx.my_bench()
               if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not damaged or ctx.defender is None:
        return
    source = await ctx.choose_pokemon(
        damaged, "Choose a Benched Pokémon to move all damage counters from")
    if source is None:
        return
    await ctx.move_damage_counters(source, ctx.defender)


card = PokemonCardDef(
    guid="906808ea-c4b0-5697-9d0e-38103089a2b9",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name",
    display_name="Liepard",
    searchable_by=["Liepard", "Stage 1", "Liepard"],
    subtypes=["Stage 1"],
    collector_number=115,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    family_id=509,
    abilities=[
        Attack(
            title="Dishonest Swap",
            game_text="Move all damage counters from 1 of your Benched Pok\u00e9mon to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=magical_echo,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)