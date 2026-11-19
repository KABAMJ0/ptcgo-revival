from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_pokemon_card


async def _call_back(ctx):
    """Call Back: a Basic or Baby from their discard onto their Bench, marked."""
    mine = ctx.my_bench()
    if len(mine) >= ctx.bench_limit(ctx.player_id):
        return
    pile = [c for c in ctx.discard_pile(ctx.opponent_id) if is_pokemon_card(c)]
    if not pile:
        return
    picked = await ctx.choose_cards(pile, 1, prompt="Choose a Basic Pokemon")
    if not picked:
        return
    card = picked[0]
    if await ctx.bench_pokemon(card):
        await ctx.deal_damage(10, target=card, apply_modifiers=False,
                              as_counters=True)


async def _surround(ctx):
    """Surround: heads Asleep, tails nails the Defending Pokemon in place."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    heads = await ctx.flip_coins(1, "Surround")
    if heads and all(heads):
        await ctx.apply_special_condition(defender, SpecialConditions.ASLEEP)
    else:
        ctx.lock_retreat(defender)

card = PokemonCardDef(
    guid="6993c7be-1f7b-5fb1-8cda-adedaf6e2e9c",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkHaunter.Name",
    display_name="Dark Haunter",
    searchable_by=["Dark Haunter", "Stage 1", "DarkHaunter"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Call Back",
            game_text="Put a Baby Pok\u00e9mon or Basic Pok\u00e9mon card from your opponent's discard pile onto his or her Bench. Put 1 damage counter on that Pok\u00e9mon. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_call_back,
        ),
        Attack(
            title="Surround",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep. If tails, the Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=20,
            effect=_surround,
        ),
    ],
)