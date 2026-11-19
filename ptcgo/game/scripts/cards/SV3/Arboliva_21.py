from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID


async def enriching_egg(ctx):
    """Heal all damage from 1 of your Benched Pokemon."""
    bench = [p for p in ctx.my_bench() if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to heal")
    if target is not None:
        await ctx.heal(ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0), target)


card = PokemonCardDef(
    guid="9e175600-e3b0-56f0-9d3b-74a12c0d0382",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arboliva.Name",
    display_name="Arboliva",
    searchable_by=["Arboliva", "Stage 2", "Arboliva"],
    subtypes=["Stage 2"],
    collector_number=21,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name",
    family_id=928,
    abilities=[
        Attack(
            title="Healing Fruit",
            game_text="Heal all damage from 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=enriching_egg,
        ),
        Attack(
            title="Oil Shot",
            cost={PokemonTypes.GRASS: 1},
            damage=90,
        ),
    ],
)