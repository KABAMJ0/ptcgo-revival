from ptcgo.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from ptcgo.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.trainers import has_energy_of
from ptcgo.game.session.passives import effective_max_hp

def _adrena_brain_condition(board, player_id, pokemon):
    """Offerable only with Darkness Energy on this Pokemon, damage on one of
    yours, and an opposing Pokemon to move it to."""
    if not has_energy_of("darkness")(pokemon):
        return False
    mine = board.pokemon_in_play(player_id)
    if not any(p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
               for p in mine):
        return False
    return any(board.pokemon_in_play(pid)
               for pid in board.player_ids if pid != player_id)


async def adrena_brain(ctx):
    """Move up to 3 damage counters from 1 of your Pokemon to 1 of your
    opponent's."""
    damaged = [p for p in ctx.my_pokemon_in_play()
               if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not damaged:
        return
    source = damaged[0] if len(damaged) == 1 else await ctx.choose_pokemon(
        damaged, "Choose a Pokémon to move damage counters from")
    if source is None:
        return
    theirs = ctx.opponent_pokemon_in_play()
    if not theirs:
        return
    dest = theirs[0] if len(theirs) == 1 else await ctx.choose_pokemon(
        theirs, "Choose a Pokémon to move damage counters to")
    if dest is None:
        return
    await ctx.move_damage_counters(source, dest, max_count=3)

card = PokemonCardDef(
    guid="54a4b752-7c1c-5a7c-98c7-9c721c8f2ebf",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munkidori.Name",
    display_name="Munkidori",
    searchable_by=["Munkidori", "Basic", "Munkidori"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=1015,
    abilities=[
        Ability(
            title="Adrena-Brain",
            game_text="Once during your turn, if this Pok\u00e9mon has any Darkness Energy attached, you may move up to 3 damage counters from 1 of your Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_adrena_brain_condition,
            effect=adrena_brain,
        ),
        Attack(
            title="Mind Bend",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)