from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

from ptcgo.game.data_utils import Activations


async def matter_exchange(ctx):
    """Discard a card from your hand to draw a card."""
    hand = [card for card in ctx.hand()]
    if not hand:
        return
    picks = await ctx.choose_cards(hand, 1, minimum=1,
                                  prompt="Choose a card to discard")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.draw_cards(1)

card = PokemonCardDef(
    guid="0fb62a92-5423-5a34-b3cb-6635d7a39b58",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkKadabra.Name",
    display_name="Dark Kadabra",
    searchable_by=["Dark Kadabra", "Stage 1", "DarkKadabra"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    family_id=63,
    abilities=[
        Ability(
            title="Matter Exchange",
            game_text="Once during your turn (before your attack), you may discard a card from your hand in order to draw a card. This power can't be used if Dark Kadabra is Asleep, Confused, or Paralyzed.",
            activation=Activations.ONCE_PER_TURN,
            effect=matter_exchange,
        ),
        Attack(
            title="Mind Shock",
            game_text="Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)