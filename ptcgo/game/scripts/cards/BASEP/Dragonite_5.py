from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

from ptcgo.game.data_utils import Activations


async def special_delivery(ctx):
    """Draw a card, then put a card from your hand on top of your deck."""
    if not await ctx.ask_yes_no("Draw a card and put one back on top of your deck?"):
        return
    await ctx.draw_cards(1)
    hand = [card for card in ctx.hand()]
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 1, minimum=1, prompt="Choose a card to put on top of your deck")
    if picks:
        await ctx.put_on_top_of_deck(picks[0])

card = PokemonCardDef(
    guid="44d15e04-fb45-5b0c-9840-5006c213b88b",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2", "Dragonite"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=149,
    abilities=[
        Ability(
            title="Special Delivery",
            game_text="Once during your turn (before your attack), you may draw a card. If you do, choose a card from your hand and put it on top of your deck. This power can't be used if Dragonite is Asleep, Confused, or Paralyzed.",
            effect=special_delivery,
        ),
        Attack(
            title="Supersonic Flight",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=flip_or_nothing(),
        ),
    ],
)