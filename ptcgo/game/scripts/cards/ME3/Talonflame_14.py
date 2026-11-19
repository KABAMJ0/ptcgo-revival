from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import (
    discard_random_from_hand, flip_gate,
)


async def _discard_from_opponent_hand(ctx):
    await discard_random_from_hand(ctx, ctx.opponent_id)


def _sky_hunt_condition(board, player_id, pokemon) -> bool:
    for other in board.player_ids:
        if other == player_id:
            continue
        hand = board.find_player_area(other, "hand")
        if hand is not None and hand.children:
            return True
    return False


card = PokemonCardDef(
    guid="65cba8da-52fd-5f37-b4cb-2b1d83e3f0a1",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    display_name="Talonflame",
    searchable_by=["Talonflame", "Stage 2", "Talonflame"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Ability(
            title="Sky Hunt",
            game_text="Once during your turn, you may use this Ability. Flip a coin. If heads, discard a random card from your opponent's hand.",
            activation=Activations.ONCE_PER_TURN,
            effect=flip_gate(_discard_from_opponent_hand),
            condition=_sky_hunt_condition,
        ),
        Attack(
            title="Fire Wing",
            cost={PokemonTypes.FIRE: 2},
            damage=110,
        ),
    ],
)