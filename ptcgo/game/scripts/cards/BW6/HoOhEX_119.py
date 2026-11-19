from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.content.definitions import Activations
from ptcgo.game.card_effects.support_common import requires_bench_space
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.session.passives import energy_provided_options


def _energy_types(ctx, card):
    """Every type an Energy card provides, after suppression/rewrite hooks."""
    return {type_value for option in energy_provided_options(ctx.board, card)
            for type_value in option}


async def _rebirth(ctx):
    """From the discard pile: heads puts this Pokemon onto the Bench and
    attaches 3 basic Energy cards of different types from the discard to it."""
    coins = await ctx.flip_coins(1, "Rebirth")
    if not coins or not coins[0]:
        return
    if not await ctx.bench_pokemon(ctx.source):
        return
    used = set()
    for _ in range(3):
        pool = [card for card in ctx.discard_pile()
                if is_basic_energy_card(card)
                and not (_energy_types(ctx, card) & used)]
        if not pool:
            break
        found = await ctx.choose_cards(
            pool, 1, minimum=0,
            prompt="Choose a basic Energy card of a different type to attach.")
        if not found:
            break
        used |= _energy_types(ctx, found[0])
        await ctx.attach_energy(found[0], ctx.source)


card = PokemonCardDef(
    guid="3ffcaaa9-d569-51fd-9810-eb4337a57a7f",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhEX.Name",
    display_name="Ho-Oh-EX",
    searchable_by=["Ho-Oh-EX", "Basic", "EX", "HoOhEX"],
    subtypes=["Basic", "EX"],
    collector_number=119,
    set_code="BW6",
    rarity=Rarities.RareUltra,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Ability(
            title="Rebirth",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your discard pile, you may flip a coin. If heads, put this Pok\u00e9mon onto your Bench and attach 3 different types of basic Energy cards from the discard pile to this Pok\u00e9mon.",
            usable_from="discard",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_bench_space(1),
            effect=_rebirth,
        ),
        Attack(
            title="Rainbow Burn",
            game_text="Does 20 more damage for each different type of basic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)