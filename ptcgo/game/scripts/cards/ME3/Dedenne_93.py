from ptcgo.game.card_effects.attacks_common import condition_attack, count_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.support_common import distribute_energy
from ptcgo.game.card_effects.trainers import basic_energy_of, pokemon_of

_BASIC_LIGHTNING = basic_energy_of("lightning")
_LIGHTNING_POKEMON = pokemon_of("lightning")


async def tail_generator(ctx):
    """Basic Lightning Energy from the discard pile, up to the Energy
    attached to all of the opponent's Pokemon, onto your Lightning ones."""
    allowed = count_energy("opponent")(ctx)
    if allowed <= 0:
        return []
    pool = [card for card in ctx.discard_pile() if _BASIC_LIGHTNING(card)]
    candidates = [p for p in ctx.my_pokemon_in_play() if _LIGHTNING_POKEMON(p)]
    if not pool or not candidates:
        return []
    picks = await ctx.choose_cards(
        pool, min(allowed, len(pool)), minimum=0,
        prompt="Choose Basic Lightning Energy cards from your discard pile",
    )
    if not picks:
        return []
    return await distribute_energy(ctx, picks, candidates)


card = PokemonCardDef(
    guid="58fc63c6-c456-5c2b-befc-8480d45e2e08",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=["Dedenne", "Basic", "Dedenne"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=702,
    abilities=[
        Attack(
            title="Tail Generator",
            game_text="Choose Basic Lightning Energy cards from your discard pile up to the amount of Energy attached to all of your opponent's Pok\u00e9mon and attach them to your Lightning Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=tail_generator,
        ),
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)