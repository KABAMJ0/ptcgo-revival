from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import distribute_energy
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.session.passives import energy_provided_options


def _energy_types(ctx, card):
    """Every type an Energy card provides, after suppression/rewrite hooks."""
    return {type_value for option in energy_provided_options(ctx.board, card)
            for type_value in option}


async def _triple_energy(ctx):
    """Search the deck for 3 basic Energy cards of different types and attach
    each wherever its owner likes."""
    used = set()
    picks = []
    for _ in range(3):
        pool = [card for card in ctx.deck()
                if is_basic_energy_card(card)
                and not (_energy_types(ctx, card) & used)]
        if not pool:
            break
        found = await ctx.choose_cards(
            pool, 1, minimum=0, display_cards=ctx.deck(),
            prompt="Choose a basic Energy card of a different type.")
        if not found:
            break
        picks.append(found[0])
        used |= _energy_types(ctx, found[0])
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())
    await ctx.shuffle_deck()


async def _heal_own_bench(ctx):
    await ctx.deal_damage()
    for pokemon in ctx.my_bench():
        await ctx.heal(40, pokemon)


card = PokemonCardDef(
    guid="971ab21f-f516-55bc-b8ac-7b088af8b5bf",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beautifly.Name",
    display_name="Beautifly",
    searchable_by=["Beautifly", "Stage 2", "Beautifly"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Triple Energy",
            game_text="Search your deck for 3 different types of basic Energy cards and attach them to your Pok\u00e9mon in any way you like. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=_triple_energy,
        ),
        Attack(
            title="Drainpour",
            game_text="Heal 40 damage from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_heal_own_bench,
        ),
    ],
)