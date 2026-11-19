from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import switch_self_attack


async def _move_energy_to_new_active(ctx, new_active):
    await ctx.move_energy_freely([ctx.attacker], [new_active], max_count=None,
                                 prompt="Choose an Energy to move")


async def _baton_pass(ctx):
    """Baton Pass: printed damage, then an optional switch that carries Energy."""
    await ctx.deal_damage()
    await switch_self_attack(damage=0, optional=True,
                             then=_move_energy_to_new_active)(ctx)

card = PokemonCardDef(
    guid="870af73b-8933-5c8a-84cd-6c8f47d0fb76",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ledian.Name",
    display_name="Ledian",
    searchable_by=["Ledian", "Stage 1", "Ledian"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name",
    family_id=165,
    abilities=[
        Attack(
            title="Comet Punch",
            game_text="Flip 4 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=20),
        ),
        Attack(
            title="Baton Pass",
            game_text="You may switch Ledian with 1 of your Benched Pok\u00e9mon. If you do, move as many Energy cards attached to Ledian as you like to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
            effect=_baton_pass,
        ),
    ],
)