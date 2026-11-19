from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.pokemon import is_energy_card
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def energy_draw_condition(board, player_id, pokemon):
    if pokemon is None or pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_energy_card(card) for card in hand.children)


async def energy_draw(ctx):
    picks = await ctx.discard_from_hand(
        1, predicate=is_energy_card, prompt="Discard 1 Energy card")
    if not picks:
        return 0
    return await ctx.draw_cards(3)

card = PokemonCardDef(
    guid="05bc15c6-56f6-5778-811c-5af63d30e400",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1", "Delcatty"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Ability(
            title="Energy Draw",
            game_text="Once during your turn (before your attack), you may discard 1 Energy card from your hand. Then draw up to 3 cards from your deck. This power can't be used if Delcatty is affected by a Special Condition.",
            effect=energy_draw,
            activation=Activations.ONCE_PER_TURN,
            condition=energy_draw_condition,
        ),
        Attack(
            title="Max Energy Source",
            game_text="Does 10 damage times the amount of Energy attached to all of your Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)