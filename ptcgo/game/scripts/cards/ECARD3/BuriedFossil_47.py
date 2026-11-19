from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.data_utils import def_for


def _reconstruction_available(board, player_id, pokemon):
    hand = board.find_player_area(player_id, "hand")
    return any(is_basic_energy_card(card) for card in (hand.children if hand else []))


def _is_omanyte_or_kabuto(card):
    name = (getattr(def_for(card.archetype_id), "display_name", "") or "").lower()
    return name.startswith("omanyte") or name.startswith("kabuto")


async def _reconstruction(ctx):
    if not any(is_basic_energy_card(card) for card in ctx.hand()):
        return
    found = await ctx.search_deck(
        _is_omanyte_or_kabuto, count=1, minimum=0,
        prompt="Search your deck for an Omanyte or Kabuto card")
    if found:
        await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="a5fa50a4-b584-595e-bf0d-6fac0b73fd36",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BuriedFossil.Name",
    display_name="Buried Fossil",
    searchable_by=["Buried Fossil", "Basic", "BuriedFossil"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    abilities=[
        Ability(
            title="Reconstruction",
            game_text="Once during your turn (before your attack), if you have a basic Energy card in your hand, you may search your deck for an Omanyte or Kabuto card, show it to your opponent, and put it into your hand. Then put a basic Energy card from your hand into your deck. Shuffle your deck afterward.",
            activation=Activations.ONCE_PER_TURN,
            condition=_reconstruction_available,
            effect=_reconstruction,
        ),
    ],
)