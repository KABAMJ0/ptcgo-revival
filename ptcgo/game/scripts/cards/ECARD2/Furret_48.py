from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.card_effects.trainers import is_energy_card
from ptcgo.game.attributes import AttrID


def _scavenger_hunt_available(board, player_id, pokemon):
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) >= 2


async def _scavenger_hunt(ctx):
    hand = ctx.hand()
    if len(hand) < 2:
        return
    picks = await ctx.choose_cards(
        hand, 2, prompt="Choose 2 cards from your hand to put into your deck")
    if picks:
        await ctx.shuffle_into_deck(picks)
    found = await ctx.search_deck(
        is_energy_card, count=1, minimum=0,
        prompt="Choose an Energy card to put into your hand")
    if found:
        await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="e6f61d38-b1ff-51f2-9ff6-d46ccd908fb7",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furret.Name",
    display_name="Furret",
    searchable_by=["Furret", "Stage 1", "Furret"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sentret.Name",
    family_id=161,
    abilities=[
        Ability(
            title="Scavenger Hunt",
            game_text="Once during your turn (before your attack), you may put 2 cards from your hand into your deck. Then, search your deck for an Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward. This power can't be used if Furret is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_scavenger_hunt_available,
            effect=_scavenger_hunt,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)