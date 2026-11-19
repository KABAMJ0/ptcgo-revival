from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.data_utils import Activations
from ptcgo.game.card_effects.pokemon import energy_provides_type


def _water_energy(card):
    return energy_provides_type(card, PokemonTypes.WATER.value)


def _has_water_in_hand(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_water_energy(c) for c in hand.children)


async def downpour(ctx):
    """Discard a Water Energy card from your hand."""
    hand = [card for card in ctx.hand() if _water_energy(card)]
    if not hand:
        return
    picks = await ctx.choose_cards(hand, 1, minimum=1,
                                  prompt="Choose a Water Energy to discard")
    if picks:
        await ctx.discard_cards(picks)


async def riptide(ctx):
    """Printed 10, then 20 more for each Water Energy in your discard pile; those
    cards are shuffled back into your deck."""
    discarded = [card for card in ctx.discard_pile() if _water_energy(card)]
    await ctx.deal_damage(10 + 20 * len(discarded))
    if discarded:
        await ctx.shuffle_into_deck(discarded)

card = PokemonCardDef(
    guid="78f37d2c-8ebb-50df-91cd-158db6b5c399",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr",
    searchable_by=["Feraligatr", "Stage 2", "Feraligatr"],
    subtypes=["Stage 2"],
    collector_number=24,
    set_code="DM",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Ability(
            title="Downpour",
            game_text="As often as you like during your turn (before your attack), you may discard a Water Energy card from your hand.",
            activation=Activations.UNLIMITED,
            condition=_has_water_in_hand,
            effect=downpour,
        ),
        Attack(
            title="Riptide",
            game_text="This attack does 20 more damage for each Water Energy card in your discard pile. Then, shuffle those cards into your deck.",
            cost={PokemonTypes.WATER: 2},
            damage=10,
            damage_operator="+",
            effect=riptide,
        ),
    ],
)