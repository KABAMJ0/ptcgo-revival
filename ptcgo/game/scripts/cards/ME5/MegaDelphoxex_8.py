from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_pokemon_card
from ptcgo.game.session.passives import effective_bench_capacity


async def trick_portal(ctx):
    """Look at the top 9, put any number of Pokemon found there onto the
    Bench, then shuffle the rest back into the deck."""
    top = ctx.deck_top(9)
    if not top:
        return
    candidates = [card for card in top if is_pokemon_card(card)]
    space = (effective_bench_capacity(ctx.board, ctx.player_id)
             - len(ctx.my_bench()))
    if candidates and space > 0:
        picks = await ctx.choose_cards(
            candidates, min(len(candidates), space), minimum=0,
            prompt="Choose any number of Pokémon to put onto your Bench",
            display_cards=top if len(candidates) < len(top) else None)
        for card in picks:
            await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="e06e7ddc-ec19-5d51-a610-26ea2593da95",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaDelphoxex.Name",
    display_name="Mega Delphox ex",
    searchable_by=["Mega Delphox ex", "Stage 2", "MEGA", "ex", "MegaDelphoxex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=8,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=350,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    family_id=655,
    abilities=[
        Attack(
            title="Trick Portal",
            game_text="Look at the top 9 cards of your deck, and you may put any number of Pok\u00e9mon you find there onto your Bench. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=trick_portal,
        ),
        Attack(
            title="Eerie Glow",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED),
        ),
    ],
)