from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _spread_bench(ctx):
    """Printed damage, then 3 damage counters across the opponent's Bench, any way they like."""
    await ctx.deal_damage()
    await ctx.place_damage_counters(3, candidates=ctx.opponent_bench())
from ptcgo.game.session.effects import is_trainer_card


async def poltergeist(ctx):
    """Opponent reveals their hand; 50 damage for each Trainer card found there."""
    cards = await ctx.reveal_hand(of_player=ctx.opponent_id)
    count = sum(1 for c in cards if is_trainer_card(c))
    await ctx.deal_damage(50 * count)


card = PokemonCardDef(
    guid="38f308e2-2988-5c0a-a740-edcc3cce43c0",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=94,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Poltergeist",
            game_text="Your opponent reveals their hand. This attack does 50 damage for each Trainer card you find there.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="x",
            effect=poltergeist,
        ),
        Attack(
            title="Hollow Dive",
            game_text="Put 3 damage counters on your opponent's Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=_spread_bench,
        ),
    ],
)