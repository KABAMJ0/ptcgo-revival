from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_attack

async def _hundred_furious_lashes(ctx):
    """30 per Grass Energy attached to itself, then it cannot use this attack
    again next turn."""
    amount = 30 * count_energy("self", PokemonTypes.GRASS)(ctx)
    if amount > 0:
        await ctx.deal_damage(amount)
    if ctx.attacker is not None:
        ctx.session.turn_state.lock_attack(ctx.attacker.entity_id,
                                           ctx.ability.ability_id)


card = PokemonCardDef(
    guid="1d9e3268-afee-500e-b558-d352b7dce346",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name",
    display_name="Tangrowth",
    searchable_by=["Tangrowth", "Stage 1", "Tangrowth"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    family_id=114,
    abilities=[
        Attack(
            title="Hundred Furious Lashes",
            game_text="Does 30 damage times the amount of Grass Energy attached to this Pok\u00e9mon. This Pok\u00e9mon can't use Hundred Furious Lashes during your next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="x",
            effect=_hundred_furious_lashes,
        ),
        Attack(
            title="Mega Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=heal_attack(30),
        ),
    ],
)