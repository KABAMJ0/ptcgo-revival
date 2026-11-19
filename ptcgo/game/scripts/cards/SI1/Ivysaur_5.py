from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


def _damaged_in_play(ctx, player_id):
    pokemon_in_play = (ctx.my_pokemon_in_play() if player_id == ctx.player_id
                       else ctx.opponent_pokemon_in_play())
    return [pokemon for pokemon in pokemon_in_play
            if pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)]


async def strange_scent(ctx):
    removed = 0
    for player_id in (ctx.player_id, ctx.opponent_id):
        if player_id is None:
            continue
        results = await ctx.flip_coins(1, "Strange Scent")
        if not results or not results[0]:
            continue
        for _counter in range(3):
            candidates = _damaged_in_play(ctx, player_id)
            if not candidates:
                break
            target = await ctx.choose_pokemon(
                candidates,
                "Choose a Pokémon to remove a damage counter from.",
                player_id=player_id,
            )
            if target is None:
                break
            removed += await ctx.heal(10, target)
    return removed

card = PokemonCardDef(
    guid="9bbff0fe-fdcf-554b-aa8e-188d591b882c",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    display_name="Ivysaur",
    searchable_by=["Ivysaur", "Stage 1", "Ivysaur"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    family_id=2,
    abilities=[
        Attack(
            title="Strange Scent",
            game_text="Each player flips a coin. Each player who gets heads chooses a total of 3 damage counters from among his or her Pok\u00e9mon and removes them. (If the player's Pok\u00e9mon have fewer total damage counters than that, he or she removes all of them.)",
            cost={PokemonTypes.GRASS: 1},
            effect=strange_scent,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
        ),
    ],
)