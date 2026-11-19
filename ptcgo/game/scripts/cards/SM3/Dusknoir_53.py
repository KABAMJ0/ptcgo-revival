from ptcgo.game.data_utils import (
    PokemonCardDef, Attack, Ability, Activations, unimplemented,
)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_bench, damage_per
from ptcgo.game.session.effects import is_basic_pokemon


async def dark_invitation(ctx):
    """Reveal the opponent's hand; put a Basic Pokemon found there onto their
    Bench and put 3 damage counters on it."""
    await ctx.reveal_hand(ctx.opponent_id)
    candidates = [card for card in ctx.hand(ctx.opponent_id)
                  if is_basic_pokemon(card)]
    if not candidates:
        return
    picked = await ctx.choose_cards(
        candidates, 1,
        prompt="Choose a Basic Pokémon to put onto your opponent's Bench")
    if not picked:
        return
    if await ctx.bench_pokemon(picked[0]):
        await ctx.deal_damage(30, target=picked[0], as_counters=True)


card = PokemonCardDef(
    guid="8b6e244b-ee14-5836-9485-12ab40973510",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=53,
    set_code="SM3",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=355,
    abilities=[
        Ability(
            title="Dark Invitation",
            game_text="Once during your turn (before your attack), you may have your opponent reveal their hand. Put a Basic Pok\u00e9mon you find there onto your opponent's Bench, and put 3 damage counters on that Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=dark_invitation,
        ),
        Attack(
            title="Mind Jack",
            game_text="This attack does 30 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), per=30, base=30),
        ),
    ],
)