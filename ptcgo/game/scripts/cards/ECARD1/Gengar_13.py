from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import AttrID
from ptcgo.game.session.passives import effective_max_hp


def _chaos_move_available(board, player_id, pokemon):
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    opponent_id = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent_id is None:
        return False
    prizes = board.find_player_area(opponent_id, "prizePile")
    if prizes is None or len(prizes.children) > 3:
        return False
    pool = board.pokemon_in_play(player_id) + board.pokemon_in_play(opponent_id)
    return len(pool) >= 2 and any(
        p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p) for p in pool)


async def _chaos_move(ctx):
    pool = ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
    sources = [p for p in pool if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not sources:
        return
    source = sources[0] if len(sources) == 1 else await ctx.choose_pokemon(
        sources, "Choose a Pokémon to move a damage counter from")
    if source is None:
        return
    targets = [p for p in pool if p is not source]
    dest = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
        targets, "Choose a Pokémon to move the damage counter to")
    if dest is not None:
        await ctx.move_damage_counters(source, dest, max_count=1)


card = PokemonCardDef(
    guid="f26d795d-eb4b-51b5-ba8d-7323b2d82b1d",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Chaos Move",
            game_text="Once during your turn (before your attack), if your opponent has 3 or fewer Prizes, you may move 1 damage counter from 1 Pok\u00e9mon (yours or your opponent's) to another (even if it would Knock Out the other Pok\u00e9mon). This power can't be used if Gengar is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_chaos_move_available,
            effect=_chaos_move,
        ),
        Attack(
            title="Hide in Shadows",
            game_text="Switch Gengar with 1 of your Benched Pok\u00e9mon, if any.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)