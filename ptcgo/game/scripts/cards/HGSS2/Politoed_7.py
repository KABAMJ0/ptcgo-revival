from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import unafflicted


def _is_water_pokemon(pokemon):
    return PokemonTypes.WATER.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def _leap_frog_available(board, player_id, pokemon):
    from ptcgo.game.card_effects.passives_common import is_in_active_spot
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    return any(_is_water_pokemon(p) for p in board.pokemon_in_play(player_id)
               if not is_in_active_spot(p))


async def _leap_frog(ctx):
    bench = [p for p in ctx.my_bench() if _is_water_pokemon(p)]
    if not bench:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose a Water Pokémon on your Bench to switch in")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="c88738e0-3bb9-55c7-b9a1-4e988a9d68a0",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Politoed.Name",
    display_name="Politoed",
    searchable_by=["Politoed", "Stage 2", "Politoed"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="HGSS2",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Ability(
            title="Leap Frog",
            game_text="Once during your turn (before your attack), you may choose a Water Pok\u00e9mon on your Bench and switch it with your Active Pok\u00e9mon. This power can't be used if Politoed is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_leap_frog_available,
            effect=unimplemented,
        ),
        Attack(
            title="Big Chorus",
            game_text="Flip a coin for each Water Pok\u00e9mon you have in play. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)