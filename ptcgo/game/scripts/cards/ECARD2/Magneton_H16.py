from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.passives_common import is_in_active_spot, unafflicted
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.session.passives import effective_pokemon_types


async def _steel_wave(ctx):
    """Printed damage, then 10 to each benched Pokemon sharing a type with the
    Defending one (no Weakness or Resistance on the bench)."""
    types_of = lambda pokemon: set(effective_pokemon_types(ctx.board, pokemon) or [])
    foe_types = types_of(ctx.opponent_active())
    await spread_damage(10, also_base=True,
                        pred=lambda p: bool(types_of(p) & foe_types))(ctx)


def _magnetic_flow_ready(board, player_id, pokemon) -> bool:
    return is_in_active_spot(pokemon) and unafflicted(board, player_id, pokemon)


async def _magnetic_flow(ctx):
    heads = await ctx.flip_coins(1, "Magnetic Flow")
    if not (heads and heads[0]):
        return
    pool = [p for p in ctx.opponent_pokemon_in_play() if ctx.attached_energies(p)]
    if len(pool) < 2:
        return
    first = await ctx.choose_pokemon(
        pool, "Choose 2 of your opponent's Pok\u00e9mon that have Energy attached")
    if first is None:
        return
    second = await ctx.choose_pokemon(
        [p for p in pool if p.entity_id != first.entity_id],
        "Choose the second Pok\u00e9mon")
    if second is None:
        return
    from_first = await ctx.choose_cards(
        ctx.attached_energies(first), 1,
        prompt="Choose 1 Energy attached to the first Pok\u00e9mon")
    from_second = await ctx.choose_cards(
        ctx.attached_energies(second), 1,
        prompt="Choose 1 Energy attached to the second Pok\u00e9mon")
    if from_first and from_second:
        await ctx.move_energy(from_first[0], second)
        await ctx.move_energy(from_second[0], first)

card = PokemonCardDef(
    guid="72eaf176-3aa7-5cdd-a284-a620a5462177",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1", "Magneton"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Magnetic Flow",
            game_text="Once during your turn (before your attack), if Magneton is your Active Pok\u00e9mon, you may flip a coin. If heads, choose 2 of your opponent's Pok\u00e9mon that have Energy cards attached to them. Choose 1 of the Energy cards attached to each of those Pok\u00e9mon and switch them between the Pok\u00e9mon. This power can't be used if Magneton is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_magnetic_flow_ready,
            effect=_magnetic_flow,
        ),
        Attack(
            title="Steel Wave",
            game_text="This attack does 10 damage to each of your opponent's Benched Pok\u00e9mon that are the same type (color) as the Defending Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=_steel_wave,
        ),
    ],
)
