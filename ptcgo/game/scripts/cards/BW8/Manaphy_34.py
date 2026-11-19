from ptcgo.game.data_utils import (unimplemented, PokemonCardDef, Attack, Ability,
                                    Triggers)
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.card_effects.passives_common import on_ko_from_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _final_wish(ctx):
    await search_to_hand(None, count=1, reveal=False)(ctx)


async def _seafaring(ctx):
    """Flip 3; one Water Energy from the discard per head, attached to the
    Bench in any way you like."""
    results = await ctx.flip_coins(3, "Seafaring")
    heads = sum(1 for r in results if r)
    if heads <= 0:
        return
    predicate = basic_energy_of("water")
    cards = [c for c in ctx.discard_pile() if predicate(c)][:heads]
    bench = ctx.my_bench()
    if not cards or not bench:
        return
    for card in cards:
        holder = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose a Benched Pok\u00e9mon to attach the Energy to")
        if holder is None:
            break
        await ctx.attach_energy(card, holder)


card = PokemonCardDef(
    guid="7d90b453-bc4c-53a4-8d97-d84ddccc3a46",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=490,
    abilities=[
        Ability(
            title="Final Wish",
            game_text="When this Pok\u00e9mon is Knocked Out by damage from an opponent's attack, search your deck for a card and put it into your hand. Shuffle your deck afterward.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=on_ko_from_attack(_final_wish),
        ),
        Attack(
            title="Seafaring",
            game_text="Flip 3 coins. For each heads, attach a Water Energy card from your discard pile to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.WATER: 1},
            effect=_seafaring,
        ),
    ],
)