from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.session.effects import is_basic_pokemon

async def _max_elixir(ctx):
    top = ctx.deck_top(6)
    basics = [card for card in top if is_basic_energy_card(card)]
    picks = await ctx.choose_cards(
        basics, 1, minimum=0,
        prompt="Choose a basic Energy card to attach it to a Benched Pokémon",
        display_cards=top)
    benched = [p for p in ctx.my_bench() if is_basic_pokemon(p)]
    if picks and benched:
        target = await ctx.choose_pokemon(
            benched, "Choose a Benched Basic Pokémon") if len(benched) > 1 else benched[0]
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="ca3e1f3e-07b4-572a-aa4d-707069c20eed",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxElixir.Name",
    display_name="Max Elixir",
    searchable_by=["Max Elixir", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=_max_elixir
)
