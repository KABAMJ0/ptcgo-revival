from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack


def _hand_above_four(board, player_id, pokemon):
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return False
    hand = board.find_player_area(opponent, "hand")
    return bool(hand) and len(hand.children) > 4


async def scornful_storm(ctx):
    hand = ctx.hand(ctx.opponent_id)
    excess = len(hand) - 4
    if excess <= 0:
        return
    await ctx.discard_from_hand(
        excess, minimum=excess, player_id=ctx.opponent_id,
        prompt="Discard cards until you have 4 cards in your hand.",
    )


card = PokemonCardDef(
    guid="538c37f4-8c23-5be4-9a09-49a8fef3771c",
    key="DV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamence.Name",
    display_name="Salamence",
    searchable_by=["Salamence", "Stage 2", "Salamence"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="DV",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=371,
    abilities=[
        Ability(
            title="Scornful Storm",
            game_text="Once during your turn (before your attack), you may have your opponent discard cards from his or her hand until he or she has 4 cards left in his or her hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_hand_above_four,
            effect=scornful_storm,
        ),
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)
