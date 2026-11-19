from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _heads_bonus(ctx):
    await ctx.deal_damage(80)


async def _tails_discard(ctx):
    await ctx.deal_damage(40)
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        await ctx.discard_energy_from(defender, 1)


card = PokemonCardDef(
    guid="c7ca7565-d40e-50d6-bd3e-0510dbfeb0a4",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unfezant.Name",
    display_name="Unfezant",
    searchable_by=["Unfezant", "Stage 2", "Unfezant"],
    subtypes=["Stage 2"],
    collector_number=82,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    family_id=519,
    abilities=[
        Attack(
            title="Tailwind",
            game_text="Attach an Energy from your hand to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_hand(),
        ),
        Attack(
            title="Feather Strike",
            game_text="Flip a coin. If heads, this attack does 40 more damage. If tails, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=flip_gate(_heads_bonus, tails=_tails_discard),
        ),
    ],
)