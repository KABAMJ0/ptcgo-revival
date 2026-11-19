from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_prizes_remaining


async def payback(ctx):
    """30 damage, plus 60 and an Energy discard off the Defending Pokemon
    while the opponent is down to their last Prize card."""
    last_prize = count_prizes_remaining("opponent")(ctx) == 1
    await ctx.deal_damage(30 + (60 if last_prize else 0))
    defender = ctx.defender
    if last_prize and defender is not None and not ctx.effects_blocked(defender):
        await ctx.discard_energy_from(
            defender, 1,
            prompt="Choose an Energy to discard from the Defending Pok\u00e9mon")

card = PokemonCardDef(
    guid="1e6d5bb9-e58f-5105-ae7b-f52057158424",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacturne.Name",
    display_name="Cacturne",
    searchable_by=["Cacturne", "Stage 1", "Cacturne"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    family_id=331,
    abilities=[
        Attack(
            title="Rapid-Fire Needles",
            game_text="Does 30 damage to 1 of your Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Payback",
            game_text="If your opponent has only 1 Prize card left, this attack does 60 more damage and discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=payback,
        ),
    ],
)