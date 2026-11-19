from ptcgo.game.card_effects.attacks_common import flip_damage_table
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def earth_rift(ctx):
    """10 damage to each of the opponent's Benched Pokemon, then a flip: on
    tails this attack can't be used during your next turn."""
    for pokemon in ctx.opponent_bench():
        await ctx.deal_damage(10, target=pokemon, apply_modifiers=False)
    results = await ctx.flip_coins(1, "Earth Rift")
    if results and not results[0] and ctx.attacker is not None \
            and ctx.ability is not None and ctx.ability.ability_id:
        state = ctx.session.turn_state
        state.attack_locks[(ctx.attacker.entity_id,
                            ctx.ability.ability_id)] = state.turn_number + 2


card = PokemonCardDef(
    guid="4cd4a0bb-c261-5d6a-a744-0915b14e99ae",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name",
    display_name="Steelix",
    searchable_by=["Steelix", "Stage 1", "Steelix"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    family_id=95,
    abilities=[
        Attack(
            title="Earth Rift",
            game_text="This attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.) Then, flip a coin. If tails, this attack can't be used during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=earth_rift,
        ),
        Attack(
            title="Iron Smash",
            game_text="Flip 2 coins. If both are heads, this attack does 50 damage plus 20 more damage. If both are tails, this attack does nothing. If 1 is heads and 1 is tails, this attack just does 50 damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_damage_table({0: -50, 1: 0, 2: 20}, coins=2, base=50),
        ),
    ],
)