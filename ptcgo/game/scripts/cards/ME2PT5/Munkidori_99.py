from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.attributes import AttrID, PokemonTypes
from ptcgo.game.card_effects.passives_common import energy_provides_type

async def adrena_brain(ctx):
    """Move up to 3 damage counters from 1 of your Pokemon to 1 of your
    opponent's Pokemon. Offered only while a Darkness Energy is attached."""
    mine = [p for p in ctx.my_pokemon_in_play()
            if ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0) >= 10]
    theirs = ctx.opponent_pokemon_in_play()
    if not mine or not theirs:
        return
    source = await ctx.choose_pokemon(mine, "Choose a Pokémon to move damage from") \
        if len(mine) > 1 else mine[0]
    if source is None:
        return
    target = await ctx.choose_pokemon(theirs, "Choose a Pokémon to move damage onto") \
        if len(theirs) > 1 else theirs[0]
    if target is None:
        return
    await ctx.move_damage_counters(source, target, max_count=3)


def adrena_brain_available(board, player_id, pokemon) -> bool:
    """Adrena-Brain needs a Darkness Energy on this Pokemon and damage to move."""
    if not any(energy_provides_type(e, PokemonTypes.DARKNESS.value)
               for e in board.attached_energies(pokemon)):
        return False
    return any(p.get_attribute(AttrID.HP, 0) < p.get_attribute(AttrID.MAX_HP, 0)
               for p in board.pokemon_in_play(player_id))


card = PokemonCardDef(
    guid="b50a57e2-d479-542c-bf73-ef5031bf78f2",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munkidori.Name",
    display_name="Munkidori",
    searchable_by=["Munkidori", "Basic", "Munkidori"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="ME2PT5",
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
            condition=adrena_brain_available,
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